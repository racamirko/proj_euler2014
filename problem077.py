__author__ = 'raca'


def generate_primes(n=1000000):
    primes = []
    prime_flags = [0] * (n + 1)
    for prime in xrange(2, n):
        if prime_flags[prime] == 0:
            primes.append(prime)
        else:
            continue
        mult = 2
        while mult * prime < n:
            prime_flags[mult * prime] = 1
            mult += 1
    return primes


primes = generate_primes()
num_combis = {}
indent_space = ''


def find_combs_for_num(x, lower_limit = 0):
    global num_combis, indent_space
    # if x in num_combis:
    #     print(indent_space+"[%d]" % num_combis[x])
    #     return num_combis[x]
    num_of_combs = 0
    for xp in primes:
        if xp < lower_limit:
            continue
        if xp > x:
            break
        # print(indent_space+'%d + ' % xp)
        rest = x - xp
        if rest > 0:
            indent_space += '\t'
            num_of_combs += find_combs_for_num(rest, xp)
            indent_space = indent_space[:-1]
        else:
            num_of_combs += 1
    # num_combis[x] = num_of_combs
    # print("[%d!]" % num_of_combs)
    return num_of_combs


def find_sums():
    for num in xrange(2, 2000):
        combs = find_combs_for_num(num)
        print("Num %d has %d combinations" % (num, combs))
        if combs > 5000:
            break


if __name__ == '__main__':
    find_sums()
