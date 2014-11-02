"""
see: http://tutorial.math.lamar.edu/Classes/CalcII/CrossProduct.aspx
and : www.blackpawn.com/texts/pointinpoly/
"""

in_fname = 'p102_triangles.txt'

def sign(val):
    if val == 0:
        return 0
    return val/abs(val)

class Vec:
    """docstring for Vec"""

    def __init__(self, x1, y1):
        self.x = float(x1)
        self.y = float(y1)

    def intensity(self):
        return ( (self.x)**2.0 + (self.y)**2.0 )**0.5

    def add(self, dx, dy):
        return Vec(self.x + dx, self.y + dy)

    def subtract(self, v):
        return Vec(self.x-v.x, self.y-v.y)

    def multiply(self, val):
        return Vec(val*self.x, val*self.y)

    def angle_between(self, v2):
        raise NotImplementedError()

    def dot_prod(self, v2):
        return self.x*v2.x+self.y*v2.y
        
    def cross(self, v2):
        assert isinstance(v2, Vec), "Ooops"
        return (self.x*v2.y - self.y*v2.x)

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pts = []
        self.pts.append(Vec(x1, y1))
        self.pts.append(Vec(x2, y2))
        self.pts.append(Vec(x3, y3))

    def null_inside(self):
        check_order = [(0,1,2), (1,2,0), (2,0,1)]
        for comb in check_order:
            gnd_vec = self.pts[comb[0]]
            other_vec = self.pts[comb[1]]
            check_vec = self.pts[comb[2]]
            # remove gnd_vector
            v = other_vec.subtract(gnd_vec)
            check = check_vec.subtract(gnd_vec)
            zero = gnd_vec.multiply(-1.0)
            m1 = v.cross(check)
            m2 = v.cross(zero)
            if sign(m1) != sign(m2):
                return False
        return True


def test_vec():
    t1 = Triangle(-340, 495, -153, -910, 835, -947)
    t2 = Triangle(-175, 41, -421, -714, 574, -645)
    if t1.null_inside() == True:
        print("First triangle correct")
    else:
        print("First traingle fails")
    if t2.null_inside() == False:
        print("Second triangle correct")
    else:
        print("Second traingle fails")



if __name__ == '__main__':
    # test_vec()
    in_data = open(in_fname)
    cnter = 0
    for line in in_data.readlines():
        vals = line.split(',')
        int_vals = map(lambda x: int(x), vals)
        t = Triangle(*int_vals)
        if t.null_inside() == True:
            cnter += 1
    print("%d triangle contains the origin" % cnter)