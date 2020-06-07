# https://projecteuler.net/problem=9

import math
import time


def naiveApproach(n):
    """Brute force approach"""

    # a is natural number start from 1
    for a in range(1, n):

        # b is natural number greater than a thus start searching from 'a'
        for b in range(a, n):

            # c is computed by taking square root of sum of squares of a and b
            c = math.sqrt(a ** 2 + b ** 2)

            # check if c>a and c>b and the condition is met for a + b + c = n
            if c > a and c > b and a + b + c == n:
                # Brute force approach takes time of O(N^2), where N = n this is too slow, bleh !!!
                return a * b * c


# https://wf9a5m75.github.io/HackerRank/projecteuler/euler009/whiteboard1.jpg
# https://wf9a5m75.github.io/HackerRank/projecteuler/euler009/whiteboard2.jpg
def optimumSolution(n):
    """Here instead of searching for a, b and c, we derive how to compute b from a and n, thus we reduce the time
    complexity from O(N^2) to O(N) """

    # we iterate till n/3, check the above links for derivation
    for a in range(1, n // 3):

        # refer above links for derivation of b
        b = (n ** 2 - 2 * a * n) // (2 * n - 2 * a)

        # since a + b + c = n
        c = n - b - a

        # check for pythagorean triplet condition
        if a ** 2 + b ** 2 == c ** 2:
            return a * b * c


if __name__ == "__main__":
    print(naiveApproach(24))  # 480
    print(naiveApproach(120))  # 49920

    start_time = time.time()
    print(naiveApproach(1000))  # 31875000
    print(time.time() - start_time)  # 0.3 seconds

    print()

    print(optimumSolution(24))  # 480
    print(optimumSolution(120))  # 49920

    start_time = time.time()
    print(optimumSolution(1000))  # 31875000
    print(time.time() - start_time)  # 0.0009 seconds
