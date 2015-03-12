import numpy as np
import string

wrd_fname = 'p042_words.txt'

def gen_triang_list(elems = 1000):
    out_list = []
    for x in xrange(1, elems):
        out_list.append((x*(x+1))/2)
    return out_list

def word_to_sum(word):
    total_sum = 0
    word = string.lower(string.strip(word))
    base_sub = ord('a')-1
    for ch in word:
        total_sum += (ord(ch) - base_sub)
    return total_sum

def find_words():
    triang_list = gen_triang_list()
    wsrc = open(wrd_fname)
    total_count = 0
    big_line = wsrc.readlines()[0]
    for line in big_line.split(","):
        line = line[1:-1]
        ws = word_to_sum(line)
        if ws in triang_list:
            total_count += 1
    print("Found %d words" % total_count)

if __name__ == '__main__':
    find_words()