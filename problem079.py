"""

"""


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

