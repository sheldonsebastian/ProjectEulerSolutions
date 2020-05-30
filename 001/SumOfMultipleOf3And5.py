# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# https://projecteuler.net/problem=1
import math


def naiveSolution(num):
    """Here we iterate in range of 1 to num and if number divisible by 3 or 5 then we add it to the
    running count. Time complexity is O(N), where N is num """
    result = 0

    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            result += i

    return result


def sum_divisible(num, by):
    range_after_division = math.floor(num / by)
    common_sum = (range_after_division * (range_after_division + 1)) / 2
    return by * common_sum


def optimumSolution(num):
    """Time complexity is O(1), oh yeah!!!"""
    num = num - 1

    # the sum of multiples of 3 are (3+6+9+12+...) if we take 3 common we get 3(1+2+3+4+5+...)
    sum_of_3 = sum_divisible(num, 3)

    # the sum of multiples of 5 are (5+10+15+20...) if we take 5 common we get 5(1+2+3+4+5+...)
    sum_of_5 = sum_divisible(num, 5)

    # we can then take the sum of 3 and 5, but we will be adding it twice since the greatest common denominator is
    # 15, so subtract that from the sum
    sum_of_15 = sum_divisible(num, 15)

    return sum_of_3 + sum_of_5 - sum_of_15


if __name__ == "__main__":
    print(naiveSolution(10))  # 23
    print(naiveSolution(49))  # 543
    print(naiveSolution(1000))  # 233168
    print(naiveSolution(8456))  # 16687353
    print(naiveSolution(19564))  # 89301183

    print()

    print(optimumSolution(10))  # 23
    print(optimumSolution(49))  # 543
    print(optimumSolution(1000))  # 233168
    print(optimumSolution(8456))  # 16687353
    print(optimumSolution(19564))  # 89301183
