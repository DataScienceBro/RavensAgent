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
import ipdb
import copy

from SemanticNetwork import SemNode, SemNet
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
        if not problem.problemType == '2x2':
            # Skip 3x3 problems (not implemented)
            return -1

        relations = {'C#': ['AB'], 'B#' : ['AC']}

        rel = {
            'A': ['B','C'],
            'B': ['1', '2', '3', '4', '5', '6'],
            'C': ['1', '2', '3', '4', '5', '6'],
        }

        dualObjectMaps = {}

        maxObjs = -1
        for node0, neighbors in rel.items():
            objs0 = len(problem.figures[node0].objects)
            objs0 = max(objs0, maxObjs)
            for node1 in neighbors:
                objs1 = len(problem.figures[node1].objects)
                maxObjs = max(objs1, maxObjs)

                key = node0 + node1

                figures = [problem.figures[fName] for fName in key]
                oMap, invOMap = extractObjectMap(figures)
                dualObjectMaps[key] = (oMap, invOMap)


        Nets = {}
        allNodes = {}

        blah = (('A', None), ('B', 'AB'), ('C', 'AC'), ('1', 'C1') , ('2', 'C2'), ())

        # compare AB TO C1, C2, C3, C4, C5, C6

        # for figName, figObj in problem.figures.items():
        Nets['A'] = SemNet.generate(problem.figures['A'], maxObjs, allNodes, None) # semnet for which all other objects will be based
        Nets['B'] = SemNet.generate(problem.figures['B'], maxObjs, allNodes, dualObjectMaps['AB'])
        Nets['C'] = SemNet.generate(problem.figures['C'], maxObjs, allNodes, dualObjectMaps['AC'])
        Nets['1'] = SemNet.generate(problem.figures['1'], maxObjs, allNodes, dualObjectMaps['C1'])
        BARelation = Nets['B'] - Nets['A']
        C1Relation = Nets['1'] - Nets['C']


        ipdb.set_trace()



        for unknownR, knownR in relations.items():
            # extrapolate object mapping/translations from given relations' figures
            for kR in knownR:
                figures = [problem.figures[fName] for fName in kR]
                oM = extractObjectMap(figures)
                dualObjectMaps[kR]



        for unknownR, knownR in relations.items():

            # extrapolate object mapping/translations from given relations' figures
            for kR in knownR:





                dim = SemNode.objectIDs

                # test = SemNet.genAdjMatInit(maxObjs)

                # for obj0, obj1 in objectMap.items():
                #     pass

        return -1

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
                if not invObjectMap[-1] == []:
                    invObjectMap[-1] = []
                invObjectMap[-1].append(name0)
                continue
            set0 = set(obj0.attributes.items())
            minDiff = None
            minDiffScore = -1
            bestPairedName = None
            for name1, obj1 in fig1.items():
                set1 = set(obj1.attributes.items())
                differences = (set1 - set0) # differences between each object within the 2 figures
                diffScore = scoreDiffs(differences, set0, set1)

                # update best diff score if applicable
                if diffScore < minDiffScore or minDiffScore == -1: # if we find an object pairing with few diffs update our objectMap
                    minDiff = differences
                    minDiffScore = diffScore
                    bestPairedName = name1

            objectMap[name0] = bestPairedName
            invObjectMap[bestPairedName] = name0
            del fig1[bestPairedName]
        # gone through all of the initial figure's objects and there's still items in fig1
        if fig1:
            # have items in fig1
            objectMap[-1] = fig1.keys()

            for k in fig.keys():
                invObjectMap[k] = -1

        return (objectMap, invObjectMap)
    else:
        print('3x3 matrix given')
        return -1

def scoreDiffs(differences, set0, set1):
    # ipdb.set_trace()
    # TODO: naive way of scoring differences
    numD = len(differences)
    return (numD * numD) / (len(set0) * len(set1))