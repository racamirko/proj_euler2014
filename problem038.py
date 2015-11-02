__author__ = 'raca'

import numpy as np


def check_pandigital(vec_nums):
    tmp_str = ''.join(map(lambda x: str(x), vec_nums))
    if len(tmp_str) != 9:
        return False, -1
    if tmp_str[0] != '9':
        return False, -1
    for i in xrange(1, 9):
        if tmp_str.find(str(i)) == -1:
            return False, -1
    return True, int(tmp_str)


def all_combs():
    cur_max = 0
    cur_i = -1
    cur_v = []
    for i in xrange(1, 100000):
        for l in xrange(2, 10):
            vec = np.array(range(1, l))
            stat, num = check_pandigital(vec*i)
            if stat and num > cur_max:
                cur_max = num
                cur_i = i
                cur_v = vec
    print("Best I could find is: %d" % cur_max)
    print("As: %d * " % cur_i),
    print(cur_v)

if __name__ == '__main__':
    all_combs()
