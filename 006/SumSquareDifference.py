# https://projecteuler.net/problem=6


# https://brilliant.org/wiki/sum-of-n-n2-or-n3/
def naiveSolution(num):
    """ We will use sum of first n natural terms formula and sum of first n^2 natural terms formula"""
    # sum of first n natural terms, we perform floor division
    n_sum = num * (num + 1) // 2
    n_sum_squared = n_sum ** 2

    # sum of square of first n terms, we perform floor division
    n_squared_sum = (num * (num + 1) * (2 * num + 1)) // 6

    # this is optimum solution since the output is computed in O(1) i.e. constant time <<DAB!!>>
    return n_sum_squared - n_squared_sum


if __name__ == "__main__":
    print(naiveSolution(10))
    print(naiveSolution(100))
