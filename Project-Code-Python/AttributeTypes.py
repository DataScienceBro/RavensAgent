from PIL import Image
import numpy as np
import ipdb

def attrGen(nodeAttrs, attrName, attrVal):
    if attrName == 'shape':
        nodeAttrs[attrName] = Shape.convert(attrVal)
    elif attrName == 'size':
        nodeAttrs[attrName] = Size.convert(attrVal)
    elif attrName == 'angle':
        nodeAttrs[attrName] = Angle.convert(attrVal)
    elif attrName == 'alignment':
        nodeAttrs[attrName] = Alignment.convert(attrVal)
    elif attrName == 'fill':
        nodeAttrs[attrName] = Fill.convert(attrVal)
    else:
        print('Unidentifiable Attribute found', attrName, attrVal)

# Shape Attribute Wrapper
class Shape:

    @staticmethod
    def convert(shapeName):
        return Shape(1, {'name': shapeName}) # optionally include sides, corners, innerAngles...

    def __init__(self, status, props):
        self.status = status
        self.props = props

    def __sub__(self, other):
        if other == 0:
            return Shape(self.status, self.props.copy())

        newStatus = self.status - other.status
        if newStatus:
            return Shape(newStatus, self.props.copy())
        elif self.props == other.props:
            return 0
        else:
            return Shape(newStatus, {'before': other.props['name'], 'after': self.props['name']})

    def __rsub__(self, other):
        if other == 0:
            return Shape(-1, self.props.copy())
        else:
            raise ValueError('Shape Subtraction: Inconsistent Types!', self, other)

# Size Attribute Wrapper
class Size:
    scale2Num = {'very small': 0, 'small': 1, 'medium': 2, 'large': 3, 'very large': 4,'huge': 5}
    # num2Scale = ['very small', 'small', 'medium', 'large', 'very large', 'huge']

    @staticmethod
    def convert(sizeName):
        return Size(1, {'size': Size.scale2Num[sizeName]})

    def __init__(self, status, props):
        self.status = status
        self.props = props

    def __sub__(self, other):
        if other == 0:
            return Size(self.status, self.props.copy())

        newStatus = self.status - other.status
        if newStatus:
            return Size(newStatus, self.props.copy())
        elif self.props == other.props:
            return 0
        else:
            return Size(0, {'size': self.props['size'] - other.props['size']})


    def __rsub__(self, other):
        if other == 0:
            return Shape(-1, self.props.copy())
        raise ValueError('Size Subtraction: Inconsistent Types!', self, other)

# Angle Attribute
class Angle:

    @staticmethod
    def convert(angle):
        return Angle(1, {'angle': angle})

    def __init__(self, status, props):
        self.status = status
        self.props = props

    def __sub__(self, other):
        if other == 0:
            return Angle(self.status, self.props.copy())

        newStatus = self.status - other.status

        if newStatus:
            return Angle(newStatus, self.props.copy())
        elif self.props == other.props:
            return 0
        else:
            return Angle(0, {'angle': (self.angle - other.angle)})


    def __rsub__(self, other):
        if other == 0:
            return Angle(-1, self.props.copy())
        raise ValueError('Angle Subtraction: Inconsistent Types!', self, other)


class Alignment: # top, bottom
    align2Num = {'top': 1, 'bottom': 0, 'right': 1, 'left': 0}

    @staticmethod
    def convert(alignName):
        alignAxes = alignName.split('-')
        vert = Alignment.align2Num[alignAxes[0]]
        horiz = Alignment.align2Num[alignAxes[1]]
        return Alignment(1, {'vertical': vert, 'horizontal': horiz})

    def __init__(self, status, props):
        self.status = status
        self.props = props

    def __sub__(self, other):
        if other == 0:
            return Alignment(self.status, self.props.copy())

        newStatus = self.status - other.status

        if newStatus:
            return Alignment(newStatus, self.props.copy())
        elif self.props == other.props:
            return 0;
        else:
            return Alignment(0, {'vertical': self.props['vertical'] - other.props['vertical'], 'horizontal': self.props['horizontal'] - other.props['horizontal']})

class Fill:
    fill2Num = {'yes': 1, 'no': 0}

    @staticmethod
    def convert(fillYN):
        return Fill(1, {'fill': Fill.fill2Num[fillYN]})

    def __init__(self, status, props):
        self.status = status
        self.props = props

    def __sub__(self, other):
        if other == 0:
            return Fill(self.status, self.props.copy())

        newStatus = self.status - other.status

        if newStatus:
            return Fill(newStatus, self.props.copy())
        elif self.props == other.props:
            return 0
        else:
            return Fill(0, {'fill'})

