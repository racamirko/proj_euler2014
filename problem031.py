"""
    In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?
"""

import numpy as np

coefs = np.array([1, 2, 5, 10, 20, 50, 100, 200])

# coefs = np.array([1, 2, 5])
num_coef = coefs.size

def find_combs(rez=200, start_idx=0):
    global coefs, num_coef
    found_combis = []
    if start_idx < num_coef:
        mult = 0
        while mult*coefs[start_idx] <= rez:
            for comb2 in find_combs(rez-mult*coefs[start_idx], start_idx+1):
                # merge combinations
                comb2[start_idx] = mult
                if (coefs*comb2).sum() == rez:
                    # print("%d =" % rez),
                    # print(comb2)
                    found_combis.append(comb2)
            mult += 1
    else:
        found_combis.append([0]*num_coef)
    return found_combis

sol = find_combs(200)
print(sol)
print(len(sol)) # 73682