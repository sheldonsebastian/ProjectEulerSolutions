# Approach #2: Recursive Approach with Memoization


def countRoutes(rows, columns, cache):
    """Supporting function which finds the number of routes based on memoization cache"""
    if rows == 0 or columns == 0:
        # if first row or first column, there is only single route from (0,0) ie all rightward motion or all downward
        # motion
        return 1
    else:
        # check if number of routes already computed
        if cache.get((rows, columns)) is not None:
            return cache[(rows, columns)]
        # does not exist so recompute
        else:
            downward_contribution = countRoutes(rows - 1, columns, cache)
            rightward_contribution = countRoutes(rows, columns - 1, cache)
            cache[(rows, columns)] = downward_contribution + rightward_contribution
            return cache[(rows, columns)]


# https://projecteuler.net/overview=015
def memoized_recursive_approach(rows, columns):
    """Since the recursive approach computes the number of routes for repeated values we store the results in cache
    dictionary and use memoization technique to solve this approach """
    cache = {}
    return countRoutes(rows, columns, cache)
