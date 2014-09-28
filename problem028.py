import numpy as np

class NextAddress:

    def __init__(self, grid_size):
        self.directions = [(1,0), (0,-1), (-1,0), (0, 1)]
        self.grid_size = grid_size
        self.origin = (grid_size/2, grid_size/2)
        self.pos = self.origin
        self.cur_radius = 0
        self.active_dir = 3

    def __iter__(self):
        return self

    def _next_coord(self):
        return self.pos[0] + self.directions[self.active_dir][0], self.pos[1] + self.directions[self.active_dir][1]

    def dist(self, c1):
        return max(abs(self.origin[0]-c1[0]), abs(self.origin[1]-c1[1]))

    def change_direction(self):
        if self.active_dir == 3:
            self.active_dir = 0
            self.cur_radius += 1
            raise StandardError()
        self.active_dir += 1


    def next(self):
        pot_next_coord = self._next_coord()
        if self.dist(pot_next_coord) > self.cur_radius:
            try:
                self.change_direction()
            except StandardError:
                self.pos = (self.pos[0], self.pos[1]+1)
                if self.pos[1]+1 > self.grid_size:
                    raise StopIteration()
                return self.pos
            pot_next_coord = self._next_coord()
        self.pos = pot_next_coord
        return self.pos



def gen_mat():
    big_mat = np.zeros((1001, 1001))
    gen_obj = NextAddress(1001)
    # initial position
    big_mat[500,500] = 1
    cnt = 2
    for coord in gen_obj:
        # print("Coords: %d, %d" % coord)
        big_mat[coord[0], coord[1]] = cnt
        cnt += 1
    return big_mat

def sum_diags(matt):
    sum1 = 0
    i = 0
    while i < matt.shape[0]:
        sum1 += matt[i,i]
        sum1 += matt[i, matt.shape[1]-i-1]
        i += 1
    sum1 -= matt[matt.shape[0]/2, matt.shape[1]/2]
    return sum1


mm = gen_mat()
# print(mm)
print(sum_diags(mm))

