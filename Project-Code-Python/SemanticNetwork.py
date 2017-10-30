from PIL import Image
import numpy as np
import copy
import ipdb

from AttributeTypes import attrGen

class SemNet:

    @staticmethod
    def generate(ravenFigure, dim, allNodes, globalIDs, aliasPair):
        adjMat = np.zeros((dim, dim), dtype=object)

        # print('got omap')
        edges = []
        locallyUsedIDs = set()

        for objName, objVal in ravenFigure.objects.items():

            node = None
            if aliasPair and aliasPair[objName] != -1:
                aliasName = aliasPair[objName]
                # print('using alias: {0}'.format(aliasName))
                node = SemNode.convert(objName, objVal, edges, allNodes[aliasName])
            else:

                if SemNode.objectIDs < dim:
                    # if generating another id category still leaves room for one more
                    node = SemNode.convert(objName, objVal, edges)
                else:
                    print('manually choosing alias for {0}\'s {1}'.format(ravenFigure.name, objName))
                    # go through all current objectIDs and choose best among unused categories
                    ipdb.set_trace()
                    for i in range(0, SemNode.objectIDs):
                        if (not i in locallyUsedIDs):
                            print('could use {0}'.format(globalIDs[i]))


                    # choose best
            try:
                adjMat[node.id][node.id] = node
                allNodes[objName]= node
                locallyUsedIDs.add(node.id)
                if not node.id in globalIDs:
                    globalIDs[node.id] = []
                globalIDs[node.id].append(objName)
            except IndexError:
                # go through all unused indicies

                print('\tNONE SEMNET GENERATED FOR ' + ravenFigure.name)
                ipdb.set_trace()
                # TODO: remove this patch and implement better object matching
                return None

        # have all nodes in Semnet now
        # have all internalLinks, so place edges now accordingly
        if edges:
            # print('edges with internal links!')
            for node0, edge, nodes1 in edges:
                nodes1 = nodes1.split(',')
                for node1 in nodes1:
                    row = allNodes[node0].id
                    col = allNodes[node1].id

                    if adjMat[row][col] and isinstance(adjMat[row][col], SemEdge):
                        # some edge already exists, so append
                        adjMat[row][col].addEdge(edge)
                    else:
                        # new edge
                        adjMat[row][col] = SemEdge.generate(edge)

                # print(node0, edge, node1)

        return SemNet(len(ravenFigure.objects), adjMat)

    def __init__(self, status, adjMat = 0):
        # print('creating semnet', type(adjMat))
        self.status = status
        self.adjMat = adjMat

    def __sub__(self, other):
        if other and isinstance(other, SemNet):
            return SemNet(self.status - other.status, self.adjMat - other.adjMat)
        else:
            return None

        # print('subtacting two sem nets', type(self.adjMat), type(other.adjMat))

    def __rsub__(self, other):
        if other and isinstance(other, SemNet):
            return other - self
        else:
            return None

    def __str__(self):
        return '\n\t{0}\n'.format(str(self.adjMat))

    def __repr__(self):
        return self.__str__()


class SemNode:
    objectIDs = 0

    @staticmethod
    def convert(objName, objVal, edges, alias = None):
        nID = None
        if alias:
            nID = alias.id
        else:
            # use the current id and then increment it for the next node to use if necessary
            nID = SemNode.objectIDs
            print('{0} is a new object: {1}'.format(objName, SemNode.objectIDs))
            SemNode.objectIDs += 1

        nodeAttrs = {}
        for attrName, attrVal in objVal.attributes.items():
            if attrName in SemEdge.edgeTerms:
                edges.append((objName, attrName, attrVal))
            else:
                attrGen(nodeAttrs, attrName, attrVal)

        return SemNode(nID, 1, nodeAttrs)

    def __init__(self, id, status, attributes):
        self.id = id
        self.status = status
        self.attributes = attributes

    def __sub__(self, other):
        if other == 0:
            return copy.deepcopy(self)

        if self.status == other.status:
            # 0 status change
            if self.id != other.id:
                raise ValueError('Node Subtraction: Incorrect Index!', self, other)

            sAttr = self.attributes
            oAttr = other.attributes
            newAttr = {}

            for attrName in sAttr:
                if attrName in oAttr:
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
            return SemNode(self.id, -1, self.attributes)
        else:
            raise ValueError('Node Subtraction: Inconsistent Types!', self, other)

    def __str__(self):
        return '\n\tID: {0}, ST: {1}, ATRS: {2}\n'.format(self.id, self.status, self.attributes)
        # return 'id:', str(self.id),'status:',str(self.status), 'attr:',str(self.attributes)

    def __repr__(self):
        return self.__str__()


class SemEdge:
    edgeTerms = {'inside', 'left-of', 'above', 'overlaps'}

    @staticmethod
    def generate(edgeType):
        return SemEdge(1, set([edgeType]))

    def __init__(self, status, attributes):
        self.status = status
        self.attributes = attributes

    def __sub__(self, other):
        if other == 0:
            return SemEdge(self.status, self.attributes.copy())

        newStatus = self.status - other.status

        if newStatus:
            return SemEdge(newStatus, self.attributes.copy())
        elif self.attributes == other.attributes:
            return 0
        elif isinstance(other, SemEdge):
            return SemEdge(0, self.attributes - other.attributes)
        else:
            return None

    def __rsub__(self, other):
        if other == 0:
            return SemEdge(-1, self.attributes.copy())
        else:
            raise ValueError('Edge Subtraction: Inconsistent Types!', self, other)

    def addEdge(self, edgeType):
        self.attributes.add(edgeType)

    def __str__(self):
        return '{0}~{1}'.format(self.status, self.attributes)

    def __repr__(self):
        return self.__str__()








