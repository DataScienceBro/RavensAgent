from PIL import Image
import numpy as np
import ipdb
import copy

from AttributeTypes import attrGen

class SemNode:
    objectIDs = 0

    @staticmethod
    def convert(ravObj, alias = None):
        nID = None
        if alias:
            nID = alias.id
        else:
            nID = SemNode.objectIDs
            SemNode.objectIDs += 1

        nodeAttrs = {}
        for attrName, attrVal in ravObj.attributes.items():
            attrGen(nodeAttrs, attrName, attrVal)

        return SemNode(nID, 1, nodeAttrs)

    def __init__(self, id, status, attributes):
        self.id = id
        self.status = status
        self.attributes = attributes

    def __sub__(self, other):
        # self - other
        # print('subtracting semnodes\n\t', self, 'and\n\t', other)
        # ipdb.set_trace()

        if other == 0:
            return copy.deepcopy(self)

        # if self == 0:
        #     return SemNode(other.id, other.attributes, -1)

        if self.status == other.status:
            # 0 status change
            print('no status change')
            if self.id != other.id:
                raise ValueError('Node Subtraction: Incorrect Index!', self, other)

            sAttr = self.attributes
            oAttr = other.attributes
            newAttr = {}

            for attrName in sAttr:
                if attrName in oAttr:
                    # print(attrName, 'is in both', sAttr, oAttr)
                    # Shape Subt, Fill Subt, Size Subt...
                    newAttr[attrName] = sAttr[attrName] - oAttr[attrName]
                else:
                    newAttr[attrName] = sAttr[attrName]


            for attrName in oAttr:
                if not attrName in sAttr:
                    newAttr[attrName] = 0 - oAttr[attrName]

            return SemNode(self.id, 0, newAttr)

        raise ValueError('Node Subtraction: Invalid Status!', self, other)

    def __rsub__(self, other):
        if other == 0:
            return SemNode(self.id, self.attributes, -1)
        else:
            raise ValueError('Node Subtraction: Inconsistent Types!', self, other)

    def __str__(self):
        return '(id{0}, st{1}) - {2}'.format(self.id, self.status, self.attributes)
        # return 'id:', str(self.id),'status:',str(self.status), 'attr:',str(self.attributes)

    def __repr__(self):
        return self.__str__()


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

    @staticmethod
    def generate(ravenFigure, dim, allNodes, dualOMaps):
        adjMat = np.zeros((dim, dim), dtype=object)

        # print('got omap')
        for objName, objVal in ravenFigure.objects.items():

            n = None
            if dualOMaps:
                aliasName = dualOMaps[1][objName]
                n = SemNode.convert(objVal, allNodes[aliasName])
            else:
                n = SemNode.convert(objVal)
            allNodes[objName]= n
            adjMat[n.id][n.id] = n
        return SemNet(adjMat)

    def __init__(self, adjMat = 0):
        # print('creating semnet', type(adjMat))
        self.adjMat = adjMat

    def __sub__(self, other):
        # print('subtacting two sem nets', type(self.adjMat), type(other.adjMat))
        return SemNet(self.adjMat - other.adjMat)

    def __rsub__(self, other):
        return other - self

    def __str__(self):
        return str(self.adjMat)

    def __repr__(self):
        return self.__str__()










