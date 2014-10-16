
combs = set()

for a in xrange(2,101):
    for b in xrange(2,101):
        combs.add(a**b)

print(len(combs)) # 9183