import numpy as np

# coefs = np.array([1, 2, 5, 10, 20, 50, 100, 200])

coefs = np.array([1, 2, 5])

def find_combs(rez=200, start_idx=0):
    global coefs
    found_combis = []
    for i in xrange(start_idx, 3):
        comb = [0]*start_idx
        mult = 0
        while mult*coefs[i] <= rez:
            for comb2 in find_combs(rez-mult*coefs[i], i+1):
                # merge combinations
                comb2[i] = mult
                if coefs*comb2 == rez:
                    print("%d =" % rez),
                    print(comb2)
                    found_combis.append(comb2)
            mult += 1
    return found_combis

print(find_combs(10))