"""
Sudoku solver.
"""

from itertools import product
from copy import deepcopy
from collections import deque

in_fname = "/home/raca/Downloads/p096_sudoku.txt"

class SudokuSolver(object):
    """docstring for SudokuSolver"""

    def __init__(self):
        self.table = {}
        self.fixed = {}
        self.checkpoints_table = deque() # table state before branching
        self.checkpoints_fixed = deque() # fixed state before branching
        self.checkpoints_bad_decision = deque() # bad decision in the current branch
        self.checkpoints_decision = deque() # branching decision
        self.checkpoints_checkpoints_decision = deque() # ha, so meta of me...
        self.bad_decisions = []
        self.guess_threshold = 2 # how many combinations we need to have to make a guess, initially just 2-uncertainty are considered
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
        self.check_inconsistent()

    def check_inconsistent(self):
        for x,y in product(range(9), repeat=2):
            if len(self.table[(x,y)]) == 0:
                print("\tDetected inconsistant state!")
                self.pop_state()

    def insert_original_table(self,lines):
        x = 0
        for line in lines:
            for y in xrange(9):
                if line[y] != '0':
                    self.add_observation(x,y,int(line[y]))
            x += 1

    def run(self, max_guesses=1000):
        guess_no = 0
        while guess_no < max_guesses: # just to avoid infinite loops and waiting
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
            table_cleared = True
            for x,y in product(range(9), repeat=2):
                if self.fixed[(x,y)] == False:
                    print("Unfinished business")
                    table_cleared = False # inconsistant state - not enough information for clear solving
                    # self.disp()
                    # self.disp_dillemas()
                    break
            if table_cleared:
                print("Done.")
                return True # success!
            else:
                try:
                    self.make_a_guess()
                except RuntimeError:
                    return False
            guess_no += 1

    def push_state(self, decision):
        self.checkpoints_decision.append(decision)
        self.checkpoints_checkpoints_decision.append(deepcopy(self.checkpoints_decision))
        self.checkpoints_fixed.append(deepcopy(self.fixed))
        self.checkpoints_table.append(deepcopy(self.table))
        self.checkpoints_bad_decision.append(deepcopy(self.bad_decisions))

    def pop_state(self):
        self.table = self.checkpoints_table.pop()
        self.fixed = self.checkpoints_fixed.pop()
        self.checkpoints_decision = self.checkpoints_checkpoints_decision.pop()
        self.bad_decisions = self.checkpoints_bad_decision.pop()
        self.bad_decisions.append(self.checkpoints_decision.pop())
        self.guess_threshold = 2
        # print("Guesses made: ")
        # print(self.checkpoints_decision)
        # print("Forbidden moves: ")
        # print(self.bad_decisions)

    def make_a_guess(self):
        while True:
            increase_thresh = True
            for x,y in product(range(9), repeat=2):
                if self.fixed[(x,y)] == False and len(self.table[(x,y)]) == self.guess_threshold:
                    # find a guess we didn't have
                    for val in self.table[(x,y)]:
                        comb_key = (x,y,val)
                        if comb_key not in self.bad_decisions:
                            print("Guessing (%d,%d) = %d" % (x+1, y+1, val))
                            self.push_state(comb_key)
                            self.add_observation(x,y,val)
                            # self.disp()
                            return
                    # we eliminated all options for a single field - meaning the error is further up
                    self.pop_state()
                    increase_thresh = False
                    break
            if increase_thresh:
                self.guess_threshold += 1
            if self.guess_threshold > 9:
                raise RuntimeError("Guess level went too high")

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
            tmpsum *= 10
            tmpsum += self.table[(0,i)][0]
        return tmpsum

in_hnd = open(in_fname)
all_lines = in_hnd.readlines()
total_solved = 0
not_solved = []
total_sum = 0
for sid in xrange(50):
    print("Solving #%02d" % (sid+1))
    solver = SudokuSolver()
    solver.insert_original_table(all_lines[sid*10+1:(sid+1)*10])
    print("Initial state:")
    solver.disp()
    if not solver.run():
        solver.disp_dillemas()
        not_solved.append(sid+1)
    else:
        total_solved += 1
        total_sum += solver.get_sum()
    solver.disp()

print("With guessing, solves: %d" % total_solved) # 50!
print("Problems: "),
print(not_solved)
print("Sum: %d" % total_sum) # 24702