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

from SemanticNetwork import SemNode, SemNet
from Transformations import ruleFuncs
# from Misc import CustomFigure, CustomObject

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # internalRelationTerms = ['inside', 'left-of', 'above', 'overlaps']


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

        if not problem.problemType == '2x2':
            # Skip 3x3 problems (not implemented)
            return -1

        challenge = problem.name.startswith('Challenge')


        rel = {
            'A': ['B','C'],
            'B': ['1', '2', '3', '4', '5', '6'],
            'C': ['1', '2', '3', '4', '5', '6'],
        }

        ansScores = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

        # GENERATE AND TEST APPROACH
        if problem.hasVisual:

            # if we find a AB relation, then we have generated a horizontal rule and test all the C#

            # if we find a AC relation, then we have generated a vertical rule and test all the B#

            aImg = np.asarray(Image.open(problem.figures['A'].visualFilename))
            aImg = (aImg > 128) * 255
            imgMatchThreshold = 0.02 * aImg.size

            rules = {}
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

            if challenge:
                sortAns = sorted(ansScores.items(), key=lambda x: x[1], reverse = True)
                if sortAns[0][1] > sortAns[1][1]:
                    return int(sortAns[0][0])
                else:
                    return -1



        # SEMANTIC NETWORK APPROACH
        if problem.hasVerbal:
            # generate object mappings between figures and identify maximum number of objects for Net dimensionality
            dualObjectMaps = {}
            maxObjs = -1
            for node0, neighbors in rel.items():
                objs0 = len(problem.figures[node0].objects)
                maxObjs = max(objs0, maxObjs)
                for node1 in neighbors:
                    objs1 = len(problem.figures[node1].objects)
                    maxObjs = max(objs1, maxObjs)

                    key = node0 + node1

                    figures = [problem.figures[fName] for fName in key]
                    oMap, invOMap = extractObjectMap(figures)
                    dualObjectMaps[key] = (oMap, invOMap)

            Nets = {}
            allNodes = {-1: None}

            netParams = (('A', None), ('B', 'AB'), ('C', 'AC'), ('1', 'C1') , ('2', 'C2'), ('3', 'C3'),('4', 'C4'), ('5', 'C5'), ('6', 'C6'))

            for netName, objPair in netParams:
                configMap = dualObjectMaps[objPair] if objPair else None
                Nets[netName] = SemNet.generate(problem.figures[netName], maxObjs, allNodes, configMap)


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

                    rowDiff = tempNet - Nets['C'] # should equal B - A
                    colDiff = tempNet - Nets['B'] # should equal C - A
                    ansScores[ansKey] += diffCompare(rowDiff, BADiff) + diffCompare(colDiff, CADiff)

        sortAns = sorted(ansScores.items(), key=lambda x: x[1], reverse = True)
        # print(sortAns)
        return int(sortAns[0][0])

# matching shapes
def extractObjectMap(figures):
    if len(figures) is 2:
        # print('extracted Object Map')
        objectMap = {}
        invObjectMap = {}
        fig0 = copy.deepcopy(figures[0].objects)
        fig1 = copy.deepcopy(figures[1].objects)

        for name0, obj0 in fig0.items():
            if not fig1:
                # if we've exhausted the result figure's objects and there's still something here
                objectMap[name0] = -1
                if -1 not in invObjectMap:
                    invObjectMap[-1] = []
                invObjectMap[-1].append(name0)
                continue

            minDiffScore = None
            bestPairedName = None
            for name1, obj1 in fig1.items():
                diffScore = 0

                o0attrs = obj0.attributes
                o1attrs = obj1.attributes

                for attr0 in o0attrs:
                    if attr0 in o1attrs:
                        diffScore -= 1.25
                        if o0attrs[attr0] == o0attrs[attr0]:
                            diffScore -= 2
                    else:
                        diffScore += 0.5
                for attr1 in o1attrs:
                    if not attr1 in o0attrs:
                        diffScore += 0.5

                # update best diff score if applicable
                if minDiffScore == None or diffScore < minDiffScore: # if we find an object pairing with few diffs update our objectMap
                    minDiffScore = diffScore
                    bestPairedName = name1

            objectMap[name0] = bestPairedName
            invObjectMap[bestPairedName] = name0
            del fig1[bestPairedName]
        # gone through all of the initial figure's objects and there's still items in fig1
        if fig1:
            # have items in fig1
            objectMap[-1] = fig1.keys()

            for k in fig1.keys():
                invObjectMap[k] = -1

        return (objectMap, invObjectMap)
    else:
        # print('3x3 matrix given')
        return -1

def diffCompare(diff0, diff1):
    # print('ANSWER MATCHING', diff0, diff1)
    if diff0 and diff1:
        totalDiff = 0

        if diff0.status == diff1.status:
            totalDiff += 17.5

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
                            totalDiff += (2 if same else -0.25)
                        else:
                            totalDiff -= 0.15
                    for attrType in attrs1:
                        if not attrType in attrs0:
                            totalDiff -=0.15
                else:
                    # SemEdge

                    diffs = (attrs0 - attrs1).union(attrs1 - attrs0)
                    totalAttrs = len(attrs0) + len(attrs1)
                    same = set.intersection(attrs0, attrs1)
                    totalDiff += (len(same) * 2) - (len(diffs) * 0.15)

            elif elem0:
                totalDiff -= 0.2
            elif elem1:
                totalDiff -= 0.2
            else:
                totalDiff += 0

        return totalDiff
    elif diff0:
        return -1 * diff0.adjMat.size
    elif diff1:
        return -1 * diff1.adjMat.size
    else:
        return 0

