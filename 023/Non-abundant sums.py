# https://projecteuler.net/problem=23
import math


def get_proper_divisors(n):
    """Get proper divisors of n"""

    proper_divisors = []
    i = 1

    # keep looping till we i is less than or equal to sqrt of n
    while i <= math.floor(math.sqrt(n)):

        # if num is divisible by i
        if n % i == 0:

            if i == (n // i):
                # to check if the divisor pairs are same or not
                proper_divisors.append(i)
            else:
                # if divisor pairs are unique
                proper_divisors.append(i)
                proper_divisors.append(n // i)
        i += 1

    # remove the num itself only if num is not 1
    if n != 1:
        proper_divisors.remove(n)

    return proper_divisors


# https://www.xarg.org/puzzle/project-euler/problem-23/
def optimumApproach(n):
    abundant_numbers = []
    # find all the abundant numbers and store them in array
    for i in range(1, n + 1):
        if sum(get_proper_divisors(i)) > i:
            abundant_numbers.append(i)

    abundant_numbers_sum = [False] * (n + 1)
    # find all numbers which are sum of 2 abundant numbers and check whether they are less than n
    for i in range(len(abundant_numbers)):
        for j in range(0, len(abundant_numbers)):
            if abundant_numbers[i] + abundant_numbers[j] <= n:
                abundant_numbers_sum[(abundant_numbers[i] + abundant_numbers[j])] = True

    result = 0
    # cannot be written as the sum of two abundant numbers
    for i in range(1, n + 1):
        if not abundant_numbers_sum[i]:
            result += i

    return result


if __name__ == "__main__":
    print(optimumApproach(10000))  # 3731004
    print(optimumApproach(15000))  # 4039939
    print(optimumApproach(20000))  # 4159710
    print(optimumApproach(28123))  # 4179871
