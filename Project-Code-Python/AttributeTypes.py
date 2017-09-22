from PIL import Image
import numpy as np
import ipdb
import copy

class SpecialDiff:
    def __init__(self, type, val):
        self.type = type

    # assume vertical symmetry
    def symmetricAngle(symmetry = 'vertSym', angle):
        return 180 - angle if vertical == 'vertSym' else 360 - angle

class Shape:
    def __init__(self, shape)

    def __sub__(self, other):
        return {}

class Angle:
    def __init__(self, angle, type=None)
        if type:
            self.type = type
        else:
            self.angle = angle

    def __sub__(self, other):
        if 180 - other.angle = self.angle and self.angle != 90:
            return SpecialDiff('angle', 'vertSym')
        elif 360 - other.angle = self.angle and self.angle != 180:
            return SpecialDiff('angle', 'horizSym')
        return {}

    def __add__(self, other):
        # angle.add(angle or dict)
        if isinstance(other, SpecialDiff) and other.type == 'angle':
            return cls(SpecialDiff.symmetricAngle(other.val, angle))
        return cls(self.angle + other.angle)

