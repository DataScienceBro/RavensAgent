from PIL import Image
import numpy as np
import ipdb
import copy

class SemNode:
    objectIDs = 0
    sizeMap = {'very small': 0, 'small': 1, 'medium': 2, 'large': 3, 'very large': 4,'huge': 5}

    def __init__(self, ravObj, alias = None):
        if not alias:
            self.id = SemNode.objectIDs
            SemNode.objectIDs += 1
        else:
            self.id = alias.id
        self.attributes = {}
        for attrName, attrVal in ravObj.items():
            if attrName is 'size':
                self.attributes['size'] = SemNode.sizeMap[attrVal]
            elif attrName is 'alignment':
                aligns = attrVal.split('-')
                self.attributes['vAlign'] = aligns[0]
                self.attributes['hAlign'] = aligns[1]
            else:
                self.attributes[attrName] = attrVal


# class SemEdge:

#     def __init__(self, status, relations):
#         self.status = status
#         self.relations = relations

#     def __sub__(self, other):
#         if other.relationType == self.relationType:
#             return SemEdge(self.status - other.status, [self.relations[key] - other.relations[key] for key in self.relations]
#         else:
#             return SemEdge(2, '<typeChange>', [other.relationType, self.relationType])

class SemNet:


    def __init__(self, rFigure, dim):
        self.adjMat = np.zeros((dim, dim), dtype=object)
        self.nodes = {}

        for objName, objVal in rFigure.objects.items():
            self.nodes[objName] = SemNode(objVal)


#     def genAdjMatInit(cls, dim):
#         return cls(np.empty((dim, dim), dtype=object))



#     def __sub__(self, other):
#         return SemNet(self.adjMat - other.adjMat)

#     def __add__(self, other):
#         return SemNet(self.adjMat + other.adjMat)

# class SemObject:
#     def __init__(self, attributes):
#         self.attributes = attributes

#     def __sub__(self, other):
#         result = {}
#         for key, val in self.attributes:
#             result[key] =


                # (A, C) => {shape: (square, circle)}
                # (B, D) => {}
                # (E, F) => {}

                 # [
                #   {
                #       A: {shape: square, fill: solid, align: topLeft},
                #       B: {shape: circle, fill: empty, align: topRight}
                #       E: {shape: triangle, above: 'a,b'}
                #   },
                #   {
                #       C: {shape: circle, fill: solid, align: topLeft},
                #       D: {shape: square, fill: empty, align: topRight},
                #       F: {shape: triangle, leftOf: 'a,b'}
                #   }
                # ]


                # cfigureList = []
                # for fName in kR:






