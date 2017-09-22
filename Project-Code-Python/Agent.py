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

        maxObjs = -1
        for node0, neighbors in rel.items():
            objs0 = len(problem.figures[node0].objects)
            objs0 = max(objs0, maxObjs)
            for node1 in neighbors:
                objs1 = len(problem.figures[node1].objects)
                maxObjs = max(objs1, maxObjs)
        ipdb.set_trace()

        objectMaps = {}
        allSemNets = {}


        # for figName, figObj in problem.figures.items():
        allSemNets['A'] = SemNet(problem.figures['A'], maxObjs)
        allSemNets['B'] = SemNet(problem.figures['A'], maxObjs, objectMaps[])

        for unknownR, knownR in relations.items():
            # extrapolate object mapping/translations from given relations' figures
            for kR in knownR:
                figures = [problem.figures[fName] for fName in kR]
                oM = extractObjectMap(figures)
                objectMaps[kR]



        for unknownR, knownR in relations.items():

            # extrapolate object mapping/translations from given relations' figures
            for kR in knownR:



                ipdb.set_trace()

                dim = SemNode.objectIDs

                # test = SemNet.genAdjMatInit(maxObjs)

                # for obj0, obj1 in objectMap.items():
                #     pass

        return -1

# matching shapes
def extractObjectMap(figures):
    if len(figures) is 2:
        print('2x2 matrix')
        objectMap = {}
        fig0 = copy.deepcopy(figures[0].objects)
        fig1 = copy.deepcopy(figures[1].objects)

        for name0, obj0 in fig0.items():
            if not fig1:
                # if we've exhausted the result figure's objects and there's still something here
                objectMap[name0] = -1
                continue
            set0 = set(obj0.attributes.items())
            minDiff = None
            minDiffIndex = -1
            bestPairedName = None
            for name1, obj1 in fig1.items():
                set1 = set(obj1.attributes.items())
                differences = (set1 - set0) # differences between each object within the 2 figures

                # naive way of calculating diff index
                numD = len(differences)
                diffIndex = (numD * numD) / (len(set0) * len(set1))

                if minDiffIndex == -1 or diffIndex < minDiffIndex: # if we find an object pairing with few diffs update our objectMap
                    minDiff = differences
                    minDiffIndex = diffIndex
                    bestPairedName = name1

            objectMap[name0] = bestPairedName
            del fig1[bestPairedName]
        # gone through all of the initial figure's objects and there's still items in fig1
        if fig1:
            # have items in fig1
            objectMap[-1] = fig1.keys()

        return objectMap
    else:
        print('3x3 matrix given')
        pass
    return -1

def getTransitions(objectMap, figures):
    if len(figures) is 2:
        for src, dst in objectMap.items():
            srcObj = figures[0][src].attributes
            dstObj = figures[1][dst].attributes
            objChanges = dict_diff(srcObj, dstObj)
            transitions = changeToTransition(objChanges)
            ipdb.set_trace()
            # attributes
    else:
        print('3x3 matrix given')
        pass
    return -1

def extractTransitions(o0):
    return -1

def changeToTransition(changes):
    transitions = {}
    if not changes:
        return transitions
    else:
        if 'shape' in changes:
            shapeVocab = ['circle', 'triangle', 'rectangle', 'square']
            transitions['shape'] = changes['shape']
        elif 'size' in changes:
            sizesVocab = ['small','medium','large','very large','huge']
            sizes = changes['size']
            sizesVocab.index(sizes[1]) - sizesVocab.index(sizes[0])


def dict_diff(first, second):
    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    # Check all keys in first dict
    for key in first:
        if (not key in second):
            diff[key] = (first[key], '<KEYNOTFOUND>')
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second:
        if (not key in first):
            diff[key] = ('<KEYNOTFOUND>', second[key])
    return diff