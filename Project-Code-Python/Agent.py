# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image
import numpy as np
import copy

import ipdb
import math
from SemanticNetwork import SemNode, SemNet
from Transformations import ruleFuncs, ruleFuncs3
from ObjectMatching import *
from VisShape import VisShape
# from Misc import CustomFigure, CustomObject

class Agent:

    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        SemNode.objectIDs = 0

        # if not problem.problemType == '2x2':

        #     # Skip 3x3 problems (not implemented)

        # if problem.name ==

        challenge = problem.name.startswith('Challenge') # no text representation

        config = (
            {
                'A': ['B','C'],
                'B': ['1', '2', '3', '4', '5', '6'],
                'C': ['1', '2', '3', '4', '5', '6'],
            },
            {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
            (('A', None), ('B', 'AB'), ('C', 'AC'), ('1', 'C1') , ('2', 'C2'), ('3', 'C3'),('4', 'C4'), ('5', 'C5'), ('6', 'C6'))
        ) if problem.problemType == '2x2' else (
            {
                'A': ['B', 'D'],
                'B': ['C', 'E'],
                'C': ['F'],
                'D': ['G', 'E'],
                'E': ['H', 'F'],
                'F': ['1', '2', '3', '4', '5', '6', '7', '8'],
                'G': ['H'],
                'H': ['1', '2', '3', '4', '5', '6', '7', '8'],
            },
            {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0},
            (('A', None), ('B', 'AB'), ('C', 'BC'), ('D', 'AD') , ('E', 'DE'), ('F', 'EF'),('G', 'DG'), ('H', 'EH'), ('1', 'H1') , ('2', 'H2'), ('3', 'H3'),('4', 'H4'), ('5', 'H5'), ('6', 'H6'), ('7', 'H7'), ('8', 'H8'))
        )

        rel, ansScores, netParams = config

        # GENERATE AND TEST APPROACH
        if problem.hasVisual:

            # try:
            ansScores = visualGenAndTest(problem, rel, ansScores)
            # except:
                # return -1

            # challenge hack
            if challenge:
                sortAns = sorted(ansScores.items(), key=lambda x: x[1], reverse = True)
                if sortAns[0][1] > sortAns[1][1]:
                    return int(sortAns[0][0])
                else:
                    return -1



        # SEMANTIC NETWORK APPROACH
        if problem.hasVerbal:
            ansScores = {key: value for key, value in ansScores.items()}
            # import ipdb; ipdb.set_trace()
            fMats = constructFigureFeatureMatrices(problem)

            # generate object mappings between figures and identify maximum number of objects for Net dimensionality
            aliasPairRef, maxObjs = matchObjects(problem, rel, fMats)

            Nets = computeSemNets(problem, aliasPairRef, maxObjs, netParams)

            ansScores = evaluateSemDiffs(problem, Nets, ansScores)


            if problem.problemType == '3x3':
                fig2ObjCnt = lambda fig: len(fig.objects)
                exactPredict = lambda actual, prediction: actual == prediction
                ansScores = numericalPredict(problem, ansScores, fig2ObjCnt, exactPredict)

        sortAns = sorted(ansScores.items(), key=lambda x: x[1], reverse = True)
        # print(sortAns)
        return int(sortAns[0][0])


def visualGenAndTest(problem, rel, ansScores):
    # if we find a AB relation, then we have generated a horizontal rule and test all the C#

    # if we find a AC relation, then we have generated a vertical rule and test all the B#
    rules = {}

    # if problem.name == 'Basic Problem D-01':
    #     ipdb.set_trace()

    if problem.problemType == '2x2':

        aImg = np.asarray(Image.open(problem.figures['A'].visualFilename))
        aImg = (aImg > 128) * 255
        imgMatchThreshold = 0.02 * aImg.size

        # generate rule
        for sibling in rel['A']:
            sibImg = np.asarray(Image.open(problem.figures[sibling].visualFilename))
            sibImg = (sibImg > 128) * 255

            for ruleName, ruleFunc in ruleFuncs.items():
                if ruleFunc(aImg, sibImg, imgMatchThreshold):
                    # print('Rule Found:', ruleName)
                    rules['A' + sibling] = ruleFunc
                    break
            # continue to next directional rule

        # test for candidates using a 3 point scale
        # candidateDiffs = {2: [], 1: [], 0: []}

        cImg = np.asarray(Image.open(problem.figures['C'].visualFilename))
        cImg = (cImg > 128) * 255
        bImg = np.asarray(Image.open(problem.figures['B'].visualFilename))
        bImg = (bImg > 128) * 255

        for ansNum in range(1,7):
            ansKey = str(ansNum)
            ansImg = np.asarray(Image.open(problem.figures[ansKey].visualFilename))
            ansImg = (ansImg > 128) * 255
            horizTest = rules['AB'](cImg, ansImg, imgMatchThreshold) if 'AB' in rules else 0
            vertTest = rules['AC'](bImg, ansImg, imgMatchThreshold) if 'AC' in rules else 0
            # candidateDiffs[horizTest + vertTest].append(str(ansNum))
            ansScores[ansKey] += horizTest * 10 + vertTest * 10
        # print(ansScores)
    else:
        # if problem.name == 'Basic Problem D-01':
        #             ipdb.set_trace()
        # if problem.name == 'Basic Problem C-12':
        #     ipdb.set_trace()
        fig2BlackPxCnt = lambda fig: np.count_nonzero(np.asarray(Image.open(fig.visualFilename).resize((46, 46))) <= 128)
        approximatePredict = lambda actual, prediction: abs(actual - prediction) < 0.08 * 46 * 46
        ansScores = numericalPredict(problem, ansScores, fig2BlackPxCnt, approximatePredict, rewardMult = 1.75)
        print('pixel count interpolation yields:', ansScores)

        rules['row'] = None
        rules['col'] = None
        rules['diag_dr'] = None
        # rules['diag_dl'] = None

        tripletPairs = [
            ('ABC', 'DEF'), # 0: row rule
            ('ADG', 'BEH'), # 1: col rule
            ('BFG', 'CDH')  # 0: downright diag rule
            # ('AFH', 'CDH')  # 0: downright diag rule
        ]
        orientation = ['row', 'col', 'diag_dr']
        size = 184 * 184
        for i, tP in enumerate(tripletPairs):
            img0 = (np.asarray(Image.open(problem.figures[tP[0][0]].visualFilename)) > 128) * 255
            img1 = (np.asarray(Image.open(problem.figures[tP[0][1]].visualFilename)) > 128) * 255
            img2 = (np.asarray(Image.open(problem.figures[tP[0][2]].visualFilename)) > 128) * 255

            img3 = (np.asarray(Image.open(problem.figures[tP[1][0]].visualFilename)) > 128) * 255
            img4 = (np.asarray(Image.open(problem.figures[tP[1][1]].visualFilename)) > 128) * 255
            img5 = (np.asarray(Image.open(problem.figures[tP[1][2]].visualFilename)) > 128) * 255

            for ruleName, ruleFunc in ruleFuncs3.items():
                # if problem.name == 'Basic Problem D-02':
                #     ipdb.set_trace()
                if ruleFunc(img0, img1, img2, size) and ruleFunc(img3, img4, img5, size):

                    # orientation = 'row' if i == 0 else 'col'
                    print('\t', orientation[i], 'Rule Found:', ruleName)
                    rules[orientation[i]] = ruleFunc
                    break

        # if problem.name == 'Basic Problem E-08':
        #     ipdb.set_trace()

        if rules['row'] != None or rules['col'] != None or rules['diag_dr'] != None:
            # found a basic row rule or col rule
            for ansNum in range(1,9):
                ansKey = str(ansNum)
                ansImg = (np.asarray(Image.open(problem.figures[ansKey].visualFilename)) > 128) * 255
                horizTest = 0
                vertTest = 0
                diag_drTest = 0

                if rules['row'] != None:
                    # if problem.name == 'Basic Problem E-01':
                    #     ipdb.set_trace()
                    # # boost the row rule suited answer
                    imgG = (np.asarray(Image.open(problem.figures['G'].visualFilename)) > 128) * 255
                    imgH = (np.asarray(Image.open(problem.figures['H'].visualFilename)) > 128) * 255

                    if rules['row'](imgG, imgH, ansImg, size):
                        # ansImage satisfies this row rule
                        horizTest = 1

                if rules['col'] != None:
                    # boost the row rule suited answer
                    imgC = (np.asarray(Image.open(problem.figures['C'].visualFilename)) > 128) * 255
                    imgF = (np.asarray(Image.open(problem.figures['F'].visualFilename)) > 128) * 255

                    if rules['col'](imgC, imgF, ansImg, size):
                        # ansImage satisfies this row rule
                        vertTest = 1

                if rules['diag_dr'] != None:
                    # boost the row rule suited answer
                    imgA = (np.asarray(Image.open(problem.figures['A'].visualFilename)) > 128) * 255
                    imgE = (np.asarray(Image.open(problem.figures['E'].visualFilename)) > 128) * 255

                    if rules['diag_dr'](imgA, imgE, ansImg, size):
                        # ansImage satisfies this row rule
                        diag_drTest = 1

                ansScores[ansKey] += horizTest * 20 + vertTest * 20 + (horizTest * vertTest) * 20 + diag_drTest * (20 if vertTest!= 0 or horizTest != 0 else 100)

        else:
            print('gotta use visshapes?')
            # ipdb.set_trace()
            # extract shapes visually use rectangularity for set equivalence,
            # vobjMap = {}
            # for figName, figObj in problem.figures.items():
            #     vobjMap[figName] = scanVisualShapes(np.asarray(Image.open(figObj.visualFilename)))





    return ansScores

def evaluateSemDiffs(problem, Nets, ansScores):
    # ipdb.set_trace()

    if problem.problemType == '2x2':

        BADiff = Nets['B'] - Nets['A']
        CADiff = Nets['C'] - Nets['A']

        bestScore = None
        bestNet = None
        for ansNum in range(1, 7):

            ansKey = str(ansNum)
            tempNet = Nets[ansKey]
            if None:
                ansScores[ansKey] += 0
                continue
            else:
                if tempNet == None:
                    ansScores[ansKey] -= 20
                else:
                    rowDiff = tempNet - Nets['C'] # should equal B - A
                    colDiff = tempNet - Nets['B'] # should equal C - A
                    ansScores[ansKey] += diffCompare(rowDiff, BADiff) + diffCompare(colDiff, CADiff)
    else:
        # TODO: only leverages bottom right 2x2 grid of 3x3 matrix, include all other figs in prediction!
        FEDiff = Nets['F'] - Nets['E']
        HEDiff = Nets['H'] - Nets['E']

        bestScore = None
        bestNet = None
        for ansNum in range(1, 9):

            ansKey = str(ansNum)
            tempNet = Nets[ansKey]
            if None:
                ansScores[ansKey] += 0
                continue
            else:
                if tempNet == None:
                    ansScores[ansKey] -= 20
                else:
                    rowDiff = tempNet - Nets['H'] # should equal F - E
                    colDiff = tempNet - Nets['F'] # should equal H - E
                    ansScores[ansKey] += diffCompare(rowDiff, FEDiff) + diffCompare(colDiff, HEDiff)

    return ansScores

def computeSemNets(problem, aliasPairRef, maxObjs, netParams):
    Nets = {}
    allNodes = {-1: None}
    globalIDs = {}

    for netName, objPair in netParams:
        # aliasPair = aliasPairRef[objPair] if objPair else None
        aliasPair = aliasPairRef[objPair] if objPair else None
        Nets[netName] = SemNet.generate(problem, netName, maxObjs, allNodes, globalIDs, aliasPair)

    # if problem.name == 'Basic Problem C-03':
    #     ipdb.set_trace()
    return Nets

def diffCompare(diff0, diff1):
    # print('ANSWER MATCHING', diff0, diff1)
    if diff0 and diff1:
        totalDiffSimilarity = 0

        if diff0.status == diff1.status:
            totalDiffSimilarity += 17.5

        for index, _ in np.ndenumerate(diff0.adjMat):
            elem0 = diff0.adjMat[index]
            elem1 = diff1.adjMat[index]
            if elem0 and elem1:
                attrs0 = elem0.attributes
                attrs1 = elem1.attributes
                if isinstance(elem0, SemNode):
                    # SemNode

                    for attrType in attrs0:
                        if attrType in attrs1:
                            # score increase
                            same = attrs0[attrType] == attrs1[attrType]
                            # print(('same' if same else 'diff'), attrType)
                            totalDiffSimilarity += (2 if same else -0.25)
                        else:
                            totalDiffSimilarity -= 0.15
                    for attrType in attrs1:
                        if not attrType in attrs0:
                            totalDiffSimilarity -=0.15
                else:
                    # SemEdge

                    diffs = (attrs0 - attrs1).union(attrs1 - attrs0)
                    totalAttrs = len(attrs0) + len(attrs1)
                    same = set.intersection(attrs0, attrs1)
                    totalDiffSimilarity += (len(same) * 2) - (len(diffs) * 0.15)

            elif elem0:
                totalDiffSimilarity -= 0.2
            elif elem1:
                totalDiffSimilarity -= 0.2
            else:
                totalDiffSimilarity += 0

        return totalDiffSimilarity
    elif diff0:
        return -1 * diff0.adjMat.size
    elif diff1:
        return -1 * diff1.adjMat.size
    else:
        return 0

def numericalPredict(problem, ansScores, fig2Num, successFunc, rewardMult = 1):
    for key, val in ansScores.items():
        ansScores[key] = round(val, 2)

    # print('\tpre-inference: {0}'.format(ansScores))
    #  do only for 3x3
    fName = ['A','B','C','D','E','F','G','H']
    arr = [fig2Num(problem.figures[f]) for f in fName]

    arr.append(None)

    arr = np.reshape(np.asarray(arr, dtype=float), (3,3))

    # print(formattedArr)

    rowPred, colPred = interpolate(arr)
    # import ipdb; ipdb.set_trace()

    # print('\tguess:{0}, {1}'.format(rowPred, colPred))

    for ansNum in range(1, 9):
        ansKey = str(ansNum)
        if successFunc(fig2Num(problem.figures[ansKey]), rowPred):
            ansScores[ansKey] += 10 * rewardMult

        if successFunc(fig2Num(problem.figures[ansKey]), colPred):
            ansScores[ansKey] += 10 * rewardMult

        if successFunc(fig2Num(problem.figures[ansKey]), rowPred) and successFunc(fig2Num(problem.figures[ansKey]), colPred):
            ansScores[ansKey] += 20 * rewardMult

    # print('\tpost-inference: {0}'.format(ansScores))

    return ansScores

# given a 3x3 array of numbers with the bottom right being nan, predict the bottom right number
def interpolate(arr):
    # import ipdb; ipdb.set_trace()
    # index of rows and cols
    index = np.asarray([0,1,2], dtype=float)

    # isolate the rows and cols as outputs of quad funcs
    yRow0 = arr[0,:]
    yRow1 = arr[1,:]
    yCol0 = arr[:,0]
    yCol1 = arr[:,1]

    # quadratic fit for each given 3 elem row and 3 elem col
    eqRow0 = np.round(np.polyfit(index, yRow0, 2) * 2) / 2
    eqRow1 = np.round(np.polyfit(index, yRow1, 2) * 2) / 2
    eqCol0 = np.round(np.polyfit(index, yCol0, 2) * 2) / 2
    eqCol1 = np.round(np.polyfit(index, yCol1, 2) * 2) / 2

    # index = np.asarray([[0],[1],[2]], dtype=float)
    rowPtrn = np.vstack((eqRow0, eqRow1, np.zeros((1,3))))
    colPtrn = np.vstack((eqCol0, eqCol1, np.zeros((1,3))))


    # row interpolation
    for i in range(rowPtrn.shape[1]):
        knownVals = rowPtrn[0:2,i]
        eq = np.round(np.polyfit(index[0:2], knownVals, 1) * 2) / 2
        rowPtrn[2,i] = np.polyval(eq, 2)

    # col interpolation
    for i in range(colPtrn.shape[1]):
        knownVals = colPtrn[0:2,i]
        eq = np.round(np.polyfit(index[0:2], knownVals, 1) * 2) / 2
        colPtrn[2,i] = np.polyval(eq, 2)

    # ipdb.set_trace()

    # row prediction of items in ?
    rowPrediction = np.polyval(rowPtrn[2,:], 2)

    # row prediction of items in ?
    colPrediction = np.polyval(colPtrn[2,:], 2)

    return (rowPrediction, colPrediction)


def scanVisualShapes(img):
    cImg = np.copy(img)
    rows, cols = cImg.shape
    vshapes = {}
    for r in range(0, rows):
        for c in range(0, cols):
            if cImg[r,c] == 0:
                vs = VisShape(r, c, cImg)
                if not vs in vshapes:
                    vshapes[vs] = 0
                vshapes[vs] += 1

    return vshapes