# Approach #3: Dynamic Programming


# http://www.robertdickau.com/lattices.html
# https://projecteuler.net/overview=015
def dynamic_programming(rows, columns):
    """The recursive approach utilizes a lot of memory since it uses recursion. We can lower the space complexity by
    using dynamic programming """

    # initialize 2D array grid of dimension (rows+1) and (columns+1)
    grid = [[0] * (rows + 1)] * (columns + 1)

    # set all columns in first column to value of 1, since we have only 1 route i.e. all downward steps
    for i in range(0, rows + 1):
        grid[i][0] = 1

    # set all rows in first row to value of 1, since we have only 1 route i.e. all rightward steps
    for i in range(0, columns + 1):
        grid[0][i] = 1

    # to find the other values we use bottom up approach, where the next value depends on previous values
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    # this approach takes O(rows*columns) time complexity
    return grid[rows][columns]
