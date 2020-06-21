# https://projecteuler.net/problem=21
import math


# https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
def get_divisors(num):
    """Get all the divisors on num without num itself"""

    divisors = []
    i = 1

    # we need to iterate only till sqrt of num
    while i <= math.floor(math.sqrt(num)):

        # if num is divisible by i
        if num % i == 0:

            if i == (num // i):
                # to check if the divisor pairs are same or not
                divisors.append(i)
            else:
                # if divisor pairs are unique
                divisors.append(i)
                divisors.append(num // i)
        i += 1

    # remove the num itself only if num is not 1
    if num != 1:
        divisors.remove(num)

    return divisors


def naiveApproach(limit):
    # iterate through all numbers and mark which numbers are amicable since if a's amicable pair is b then don't
    # recompute this again, memoization
    amicable = [0 for _ in range(limit + 1)]

    # to check if amicable or not we need to compute all the divisors of the number
    for i in range(1, limit + 1):

        # do computation only if index is not seen
        if amicable[i] == 0:

            divisors = get_divisors(i)
            pair1 = sum(divisors)

            divisors_pair = get_divisors(pair1)
            pair2 = sum(divisors_pair)

            if pair2 == i and pair1 != pair2:
                # amicable, thus set flag to 1 in the list
                amicable[pair1] = 1
                amicable[pair2] = 1

    # get the sum
    result = sum([i for i, x in enumerate(amicable) if x == 1])

    # return the result. This approach is O(n*sqrt(n)) since we are computing divisors in sqrt(n) but we do it twice
    # so 2*sqrt(n) and we repeat this n times
    return result


if __name__ == "__main__":
    print(naiveApproach(1000))  # 504
    print(naiveApproach(2000))  # 2898
    print(naiveApproach(5000))  # 8442
    print(naiveApproach(10000))  # 31626
