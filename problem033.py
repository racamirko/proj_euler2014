__author__ = 'raca'

'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''


def lct(num, denom):
    found_divisor = True
    while found_divisor:
        found_divisor = False
        smaller_value = min(num, denom)+1
        for divisor in xrange(2, smaller_value):
            if num % divisor == 0 and denom % divisor == 0:
                num /= divisor
                denom /= divisor
                found_divisor = True
                break
    return num, denom


def lct_divisor(denom1, denom2):
    found_divisor = True
    total_divisor = 1
    while found_divisor:
        found_divisor = False
        smaller_value = min(denom1, denom2)
        for divisor in xrange(2, smaller_value):
            if denom1 % divisor == 0 and denom2 % divisor == 0:
                denom1 /= divisor
                denom2 /= divisor
                total_divisor *= divisor
                found_divisor = True
                break
    return divisor


def main_cycle():
    final_denom, final_num = 1, 1
    for denom in xrange(10, 100):
        denom_str = str(denom)
        for num in xrange(10, denom):
            num_str = str(num)
            aimed_value = float(num)/float(denom)
            if num_str[0] == denom_str[1] and denom_str[0] != '0':
                val2 = float(num_str[1])/float(denom_str[0])
                if val2 == aimed_value:
                    print("Found one: %d/%d = %s/%s" % (num, denom, num_str[1], denom_str[0]))
                    num, denom = lct(num, denom)
                    print("After lct: %d/%d" % (num, denom))
                    final_num *= num
                    final_denom *= denom
            elif num_str[1] == denom_str[0] and denom_str[1] != '0':
                val2 = float(num_str[0])/float(denom_str[1])
                if val2 == aimed_value:
                    print("Found one: %d/%d = %s/%s" % (num, denom, num_str[0], denom_str[1]))
                    num, denom = lct(num, denom)
                    print("After lct: %d/%d" % (num, denom))
                    final_num *= num
                    final_denom *= denom
    print("Final product: %d/%d" % (final_num, final_denom))
    final_num, final_denom = lct(final_num, final_denom)
    print("Final product in LCT: %d/%d" % (final_num, final_denom))


if __name__ == '__main__':
    main_cycle()
    # print "Hello world"