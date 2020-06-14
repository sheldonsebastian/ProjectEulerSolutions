# Approach #4: Combinatorics Approach ==> Optimum Solution
import math


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# https://www.mathsisfun.com/combinatorics/combinations-permutations.html
# https://www.mathwarehouse.com/probability/permutations-repeated-items.php
def optimumSolution(rows, columns):
    """The recursive and dynamic programming approaches take O(rows*columns) time complexity. We can use
    combinatorics to get results in O(n) time i.e. linear time and constant space. If we have a grid of size mxn then
    we will have m rightward steps and n downward steps. Thus all possible routes will be of length m+n. We can use
    permutations formula such that P(m+n, m+n) i.e. for m+n route we have m+n steps. Since we have m repeated
    rightward steps and n repeated downward steps. Then we divide by m! and n! to account for these repetitions. """

    numerator = factorial(rows + columns)
    denominator = factorial(rows) * factorial(columns)

    # formula is math.ceil(((rows+columns)!)/((rows)!*(columns)!))
    return math.floor(numerator / denominator)
