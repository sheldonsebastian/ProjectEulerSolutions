#!/bin/python3

import math

if __name__ == "__main__":
    global_n = 2000000
    size = global_n + 1
    isprime = [True] * size
    sums_index_inclusive = [0] * size

    # mark all composites as false
    for p in range(2, int(math.sqrt(size)) + 1):
        if isprime[p]:
            for i in range(p * p, size, p):
                isprime[i] = False

    s = 0
    for p in range(2, size):
        if isprime[p]:
            s += p
        # update sum till we have seen
        sums_index_inclusive[p] = s

    # driver
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(sums_index_inclusive[n])
