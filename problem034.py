__author__ = 'raca'

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def fact(x):
    prod = 1
    for i in xrange(2, x+1):
        prod *= i
    return prod


def split_nums(x):
    x = int(x)
    out = []
    while x > 0:
        out.append(x % 10)
        x /= 10
    return out

total_sum = 0

for i in xrange(10, 1000000):
    parts = split_nums(i)
    facts = map(lambda x: fact(x), parts)
    summ = reduce(lambda x, y: x+y, facts)
    if summ == i:
        total_sum += i
        print("Good number: %d" % i)

print(total_sum) # 40730