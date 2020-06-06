# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the
# 10001st prime number?

import math


def isPrime(num):
    """we need to perform division only till we square root of num, because for any composite number we can have
    maximum one prime number greater than square root of the number """

    # we check if number is even
    if num % 2 == 0:
        return False

    # every composite number can have maximum one prime number above the square root of number itself.
    limit = math.floor(math.sqrt(num))

    # we perform division to check for primality starting from 3
    divisor = 3

    while divisor <= limit:
        if num % divisor == 0:
            # if num is divisible by divisor then num is not prime
            return False
        # check for all odd numbers
        divisor += 2

    # return True since num itself is a prime number
    return True


def naiveApproach(count_limit):
    """Find all the primes until the count is reached"""

    # we already set number 2 as prime, thus initialize count = 1
    count = 1

    # we start checking for primes after 3
    num = 3

    while count < count_limit:

        # check if number is prime or not
        if isPrime(num):
            # if prime then increment count
            count += 1

            # once count is reached then break
            if count == count_limit:
                break

        # increment num
        num += 1

    # naive approach is manageable having time complexity of O(N * sqrt(N))
    return num


if __name__ == "__main__":
    print(naiveApproach(6))  # 13
    print(naiveApproach(10))  # 29
    print(naiveApproach(100))  # 541
    print(naiveApproach(1000))  # 7919
    print(naiveApproach(10001))  # 104743
