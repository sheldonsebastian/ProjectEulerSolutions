# https://projecteuler.net/problem=20


def naiveApproach(num):
    """ To find the factorial of a number, we can recursion but that will take too long, since we will be computing
    the intermediate values repeatedly which will slow the run time and also cause recursion depth error for large
    numbers. Instead we use for loop to get the factorial"""

    result = 1
    for i in range(1, num + 1):
        result *= i

    return sum(map(int, str(result)))


if __name__ == "__main__":
    print(naiveApproach(10))  # 27
    print(naiveApproach(100))  # 648
