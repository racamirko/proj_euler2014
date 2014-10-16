"""
Sudoku solver.
"""

from itertools import product

in_fname = "/home/raca/Downloads/p096_sudoku.txt"

class SudokuSolver(object):
    """docstring for SudokuSolver"""

    def __init__(self):
        self.table = {}
        self.fixed = {}
        for x,y in product(range(9), repeat=2):
            self.table[(x,y)] = range(1,10)
            self.fixed[(x,y)] = False

    def add_observation(self, x, y, val):
        self.table[(x,y)] = [val]
        self.fixed[(x,y)] = True
        # line information
        for runner in xrange(9):
            try:
                if not self.fixed[(x,runner)]:
                    self.table[(x, runner)].remove(val)
            except ValueError:
                pass
            try:
                if not self.fixed[(runner, y)]:
                    self.table[(runner, y)].remove(val)
            except:
                pass
        # quadrant
        x_range_start = x - (x % 3)
        y_range_start = y - (y % 3)
        for x1,y1 in product(range(x_range_start, x_range_start+3), range(y_range_start, y_range_start+3)):
            try:
                if not self.fixed[(x1,y1)]:
                    self.table[(x1,y1)].remove(val)
            except KeyError:
                pass
            except ValueError:
                pass

    def insert_original_table(self,lines):
        x = 0
        for line in lines:
            for y in xrange(9):
                if line[y] != '0':
                    self.add_observation(x,y,int(line[y]))
            x += 1

    def run(self):
        new_information = True
        while new_information:
            new_information = False
            for x,y in product(range(9), repeat=2):
                if self.fixed[(x,y)] == False and len(self.table[(x,y)]) == 1:
                    print("New automatic observation at (%d, %d) = %d" % (x+1,y+1, self.table[(x,y)][0]))
                    self.add_observation(x,y,self.table[(x,y)][0])
                    new_information = True
                    # self.disp() # debug!
                    break
        # final check
        print("No new information")
        for x,y in product(range(9), repeat=2):
            if self.fixed[(x,y)] == False:
                print("Unfinished business")
                return False # inconsistant state - not enough information for clear solving
        print("Done.")
        return True # success!

    def disp(self):
        print("-" * 21)
        for x,y in product(range(9), repeat=2):
            if self.fixed[(x,y)]:
                print(self.table[(x,y)][0]),
            else:
                print("_"),
            if y in (2, 5):
                print("|"),
            if y == 8:
                print("\n")
            if y == 8 and x in (2, 5):
                print("-" * 21)
        print("-" * 21)

    def disp_dillemas(self):
        for x,y in product(range(9), repeat=2):
            if not self.fixed[(x,y)]:
                print("(%d, %d) = " % (x+1, y+1)),
                print(self.table[(x,y)])

    def get_sum(self):
        tmpsum = 0
        for i in xrange(3):
            tmpsum += self.table[(0,i)][0]
        return tmpsum

in_hnd = open(in_fname)
all_lines = in_hnd.readlines()
total_solved = 0
for sid in xrange(50):
    print("Solving #%02d" % (sid+1))
    solver = SudokuSolver()
    solver.insert_original_table(all_lines[sid*10+1:(sid+1)*10])
    print("Initial state:")
    solver.disp()
    if not solver.run():
        solver.disp_dillemas()
    else:
        total_solved += 1
    solver.disp()

print("Simple stuff solves: %d" % total_solved)