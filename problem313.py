import itertools as it

__author__ = 'raca'

horizontal_step = [0, 1]
vertical_step = [1, 0]


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


primes = generate_primes(100)
primes = map(lambda x: x ** 2, primes)


def is_prime_squared(x):
    global primes
    return x in primes


def get_min_moves(m, n):
    move_count = 0
    # to get the empty space to the red block
    move_count += m-2+n-1
    # horizontal moves
    move_count += 1+5*(m-1)
    # vertical moves
    move_count += 6+5*(n-2)
    return move_count


def get_min_moves_simulation(m, n):
    global horizontal_step, vertical_step
    move_count = 0
    space_pos = [m, n]
    # move the empty space to the red
    while space_pos != [1, 2] and space_pos != [2, 1]:
        if space_pos[0] > space_pos[1]:
            if space_pos[0] > 1:
                space_pos[0] -= 1
            else:
                space_pos[1] -= 1
        else:
            if space_pos[1] > 1:
                space_pos[1] -= 1
            else:
                space_pos[0] -= 1
        move_count += 1
    if space_pos == [1, 2]:
        dot_pos, emp_pos, num_hor_moves = move_dot([1, 1], [1, 2], horizontal_step, [m, n])
        move_count += num_hor_moves
        dot_pos, emp_pos, num_hor_moves = move_dot(dot_pos, emp_pos, vertical_step, [m, n])
        move_count += num_hor_moves
    else:
        dot_pos, emp_pos, num_hor_moves = move_dot([1, 1], [1, 2], horizontal_step, [m, n])
        move_count += num_hor_moves
        dot_pos, emp_pos, num_hor_moves = move_dot(dot_pos, emp_pos, vertical_step, [m, n])
        move_count += num_hor_moves
    return move_count


def move_dot(dot_pos, empty_space_position, direction, size_table):
    num_moves = 0
    emp_pose = empty_space_position
    goal = add_coords(dot_pos, direction)
    while goal[0] <= size_table[0] and goal[1] <= size_table[1]:
        num_moves += move_empty_spaces(emp_pose, goal, dot_pos, size_table)
        num_moves += 1
        emp_pose = dot_pos
        dot_pos = goal
        goal = add_coords(dot_pos, direction)
    return dot_pos, emp_pose, num_moves


def add_coords(pos, add):
    return [pos[0]+add[0], pos[1]+add[1]]


def move_empty_spaces(start, goal, fixed_pos, size_table):
    # breath-first search
    num_moves = 0
    q = [start]
    while goal not in q:
        q_next = []
        for pt in q:
            q_next.extend(neighbors(pt, fixed_pos, size_table))
        q = q_next
        num_moves += 1
    return num_moves


def neighbors(pt, fixed, size_table):
    ns = []
    for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        next_pt = add_coords(pt, [dx, dy])
        if next_pt != pt and next_pt != fixed and \
           next_pt[0] <= size_table[0] and next_pt[1] <= size_table[1]\
           and next_pt[0] > 0 and next_pt[1] > 0:
            ns.append(next_pt)
    return ns

if __name__ == '__main__':
    cnt_tables = 0
    for m, n in it.product(xrange(2, 20), xrange(2, 20)):
        min_moves = get_min_moves_simulation(m, n)
        print("%d, %d solves in %d" % (m, n, min_moves))
        if min_moves in primes:
            cnt_tables += 1
        if min_moves ** 0.5 > 10e5:
            break
    print("Found %d tables" % cnt_tables)
