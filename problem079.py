"""

"""
import numpy as np

fname = "/home/raca/p079_keylog.txt"

data = open(fname).readlines()
data = map(lambda x: x.strip(), data)

cur_key = ""

def insert_key(key):
    global cur_key
    end_limit = len(cur_key)
    for key_idx in xrange(len(key)-1, -1, -1):
        ch = key[key_idx]
        idx = cur_key.rfind(ch, 0, end_limit)
        if idx == -1:
            cur_key = cur_key[:end_limit] + ch + cur_key[end_limit:]
        else:
            # cur_key = cur_key[:idx] + ch + cur_key[idx:]
            end_limit = idx

def fill_left(vec, idx):
    vec[:idx] = False
    return vec

def fill_right(vec, idx):
    vec[idx:] = False
    return vec

fill_rules = {
    0: { 1: fill_left, 2:fill_left},
    1: { 0: fill_right, 2:fill_left},
    2: { 0: fill_right, 1:fill_right}
}

def first_true(vec):
    for i in xrange(len(vec)):
        if vec[i] == True:
            return i
    return -1

def insert_key2(key):
    global cur_key
    key_vec = np.array(list(cur_key))
    missing = []
    present = []
    pres_loc = {}
    for c_i in xrange(len(key)):
        found_loc = cur_key.find(key[c_i])
        if found_loc == -1:
            missing.append(c_i)
        else:
            present.append(c_i)
            pres_loc[c_i]=found_loc
    for c_i in xrange(len(key)):
        if c_i not in missing:
            continue
        if len(cur_key) == 0:
            cur_key += key[c_i]
            present.append(c_i)
            pres_loc[c_i] = 0
        options = np.array([True]*len(cur_key))
        # narrow down the locations
        for cp_i in present:
            options = fill_rules[cp_i][c_i](options, pres_loc[cp_i])
        final_idx = first_true(options)
        if final_idx == -1:
            cur_key.append += key[c_i]
            pres_loc[c_i] = len(cur_key)-1
        else:
            cur_key = cur_key[:final_idx] + key[c_i] + cur_key[final_idx:]
            pres_loc[c_i] = final_idx
        present.append(c_i)




def check_key(key):
    global cur_key
    last_idx = -1
    for char in key:
        idx = cur_key.find(char, last_idx+1)
        if idx == -1:
            return False
        else:
            last_idx = idx
    return True

for line in data:
    print(line)
    if not check_key(line):
        insert_key(line)
        print("\t%s" % cur_key)


print("Key %s" % cur_key)
print("Length: %d" % len(cur_key))

