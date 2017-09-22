from PIL import Image, ImageChops
import numpy as np
import ipdb
import copy


class CustomFigure:
    def __init__(self, ravFig):
        customObjects = {}
        for objName, objAttr in ravFig.objects:

        self.objects = ravFig.objects
        self.name = ravFig.name
        self.image = Image.open(ravFig.visualFilename)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            ipdb.set_trace()
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class CustomObject:
    objectIDs = 0
    sizeMap = {'very small': 0, 'small': 1, 'medium': 2, 'large': 3, 'very large': 4,'huge': 5}

    def __init__(self, ravObj, alias = None)
        if not alias:
            self.id = cls.objectIDs
            cls.objectIDs += inc
        else:
            self.id = alias.id
        self.attributes = {}
        for attrName, attrVal in ravObj.items():
            if attrName is 'size':
                self.attributes['size'] = sizeMap[attrVal]
            elif attrName is 'alignment':
                aligns = attrVal.split('-')
                self.attributes['vAlign'] = aligns[0]
                self.attributes['hAlign'] = aligns[1]
            else:
                self.attributes[attrName] = attrVal





