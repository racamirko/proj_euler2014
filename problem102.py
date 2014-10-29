"""
see: http://tutorial.math.lamar.edu/Classes/CalcII/CrossProduct.aspx
and : www.blackpawn.com/texts/pointinpoly/
"""

import numpy as np
import math

in_fname = '/home/raca/Downloads/p102_triangles.txt'

class Vec:
    """docstring for Vec"""

    def __init__(self, x1, y1, x2, y2):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)

    def intensity(self):
        return ( (self.x1-self.x2)**2.0 + (self.y1-self.y2)**2.0 )**0.5

    def translate(self, dx, dy):
        return Vec(self.x1 + dx, self.y1 + dy, self.x2 + dx, self.y2 + dy)

    def ground_vec(self):
        return Vec(0.0, 0.0, self.x2-self.x1, self.y2-self.y1)

    def end_pt(self):
        return self.x2, self.y2

    def dist_origs(self, v2):
        return self.x1 - v2.x1, self.y1 - v2.y1

    def angle_between(self, v2):
        return math.acos(self.dot_prod(v2)/(self.intensity()*v2.intensity()))

    def dot_prod(self, v2):
        v1_gnd = self.ground_vec()
        v2_gnd = v2.ground_vec()
        return v1_gnd.x2*v2_gnd.x2+v1_gnd.y2*v2_gnd.y2
        
    def cross(self, v2):
        assert isinstance(v2, Vec), "Ooops"
        i_v1 = self.intensity()
        i_v2 = v2.intensity()
        angle = self.angle_between(v2)
        return i_v1*i_v2*math.sin(angle)

def test_vec():
    v1 = Vec(-1, -1, 3, -1)
    v2_zero = Vec(-1, -1, 0, 0)
    v2_lower = Vec(-1, -1, -2.113434, -2.5)
    print("First mult: %.3f" % v1.cross(v2_zero) )
    print("First mult: %.3f" % v1.cross(v2_lower) )

if __name__ == '__main__':
    test_vec()