# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math


def naiveApproach():
    """Solved it using hand by using the LCM technique, and got the result. But for a scalable solution refer
    optimumSolution """
    # N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 = 232792560
    pass


def get_prime_numbers(limit):
    """To generate prime numbers less than and equal to 'limit' we use Sieve of Eratosthenes algorithm O(n*log(log(n))).
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/ """

    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    prime_array = [True for _ in range(0, limit + 1)]

    # we find prime numbers starting from 2
    prime_number = 2

    # Since the composite numbers less than square(prime_number), will have atleast one prime factor less than p,
    # thus the will already be marked in prime_array
    while prime_number * prime_number <= limit:

        # If prime_array[prime_number] is not changed, then it is a prime
        if prime_array[prime_number]:

            # Update all multiples of prime_number (thus increment the for loop by p) starting from p*p upto and
            # including n
            for i in range(prime_number * prime_number, limit + 1, prime_number):
                prime_array[i] = False

        # find the next prime number by incrementing variable by 1
        prime_number += 1

    # return all numbers whose value is True in the list
    return [p for p in range(2, limit + 1) if prime_array[p]]


# https://projecteuler.net/overview=005
def optimumSolution(upper_limit):
    """ Any number is made up of prime factors. Now since for a number to be divisible by all numbers in range of (1
    to k), it should be divisible by prime numbers in that range such that, using only prime numbers we can recreate
    all the numbers in that range. 'Any prime number P raised to power X should be less than the upper_limit',
    since then it cannot be range of the upper limit """

    # get all the prime numbers less than or equal to upper_limit
    prime_number_array = get_prime_numbers(upper_limit)

    # array to track all the exponents of the prime numbers
    exponent_array = [0] * len(prime_number_array)

    for i in range(len(prime_number_array)):
        # if the square of the prime number is greater than limit then no point searching for other exponents,
        # thus set the exponent to 1
        if prime_number_array[i] ^ 2 > upper_limit:
            exponent_array[i] = 1
        else:
            # since prime[i]^exponent[i] = upper_limit, taking log to base 2 on both sides, then shifting log(prime[
            # i]) to RHS and taking floor, we get the following equation:
            exponent_array[i] = math.floor(math.log(upper_limit, 2) / math.log(prime_number_array[i], 2))

    least_common_multiple = 1
    for i in range(len(prime_number_array)):
        # compute the result
        least_common_multiple *= prime_number_array[i] ** exponent_array[i]

    return least_common_multiple


if __name__ == "__main__":
    print(optimumSolution(10))  # 2520
    print(optimumSolution(20))  # 232792560
