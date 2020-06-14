# Approach #1: Recursive Approach


# http://www.robertdickau.com/lattices.html
# https://projecteuler.net/overview=015
def recursive_approach(rows, columns):
    """Here we will use recursive approach. The number_of_routes((0,0),(m,n)) = number_of_routes((0,0),(m-1,
    n)) + number_of_routes((0,0),(m,n-1)). We are restricted to moves only in downward or rightward direction. When
    we reach at (0, x) row or (x,0) column there is only one route to reach to these nodes from (0,0) i.e. all
    downward steps or all rightward steps. """
    if rows == 0 or columns == 0:
        # there is only one route for a node in 0th row from the (0,0) node and one route for a node in 0th column
        # from the (0,0) node
        return 1
    else:
        # recursive approach
        downward_contribution = recursive_approach(rows - 1, columns)
        rightward_contribution = recursive_approach(rows, columns - 1)

        # this approach is very slow and it REPEATS calculation for multiple nodes
        # this takes O(m,n) time
        return downward_contribution + rightward_contribution
