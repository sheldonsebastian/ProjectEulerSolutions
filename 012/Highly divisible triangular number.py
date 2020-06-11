# https://projecteuler.net/problem=12
import math


def naiveApproach(num_of_divisors):
    """Create all the triangle numbers till infinity until the condition is satisfied. The condition is that the
    number of factors for a number should be greater than or equal to the num_of_divisors variable """

    # triangle numbers are natural numbers
    triangle_number = 1

    # add natural number to the triangle number to next triangle number
    natural_number = 2

    while True:

        # initialize count of divisors with 1, since 1 divides all numbers
        count_of_divisors = 1

        # find all the factors for triangle_number
        for i in range(1, triangle_number):
            if triangle_number % i == 0:
                # increment count of divisors
                count_of_divisors += 1

        # if the count of divisors is greater than limit then break
        if count_of_divisors >= num_of_divisors:
            break

        # update triangle number
        triangle_number += natural_number

        # increment natural number
        natural_number += 1

    # very slow algorithm does not converge and give answer
    return triangle_number


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


def get_divisors_count(number):
    # get prime numbers upto sqrt of number, since for a composite number we will atmost 1 prime factor above the
    # sqrt of composite number
    primes = get_prime_numbers(math.floor(math.sqrt(number)) + 1)

    # since 1 is divisor for all start with divisor count = 1
    divisor_count = 1

    # iterate through all primes
    for prime in primes:

        exponent_count = 0

        # check if the prime number divides the composite number or not
        while number % prime == 0:
            # increment exponent counter
            exponent_count += 1

            # divide the number by prime number
            number //= prime

        if exponent_count != 0:
            # multiply the divisor count by (exponent + 1)
            divisor_count *= (exponent_count + 1)

    return divisor_count


# https://projecteuler.net/overview=012
def optimumSolution(num_of_divisors):
    """We can find all the prime factors of a triangle number in the form of p1^a * p2^b * p3^c * ... =
    triangle_number. Then we can find the number of divisors of a triangle number by (a+1)*(b+1)*(c+1)... This works
    because we are finding all combination of exponent numbers starting from 0 (that is why we added 1) upto the
    exponent value itself."""

    # find triangle numbers starting from index 1
    t = 1
    n = 2

    while True:

        # number of divisors for t
        divisors_t = get_divisors_count(t)

        if divisors_t >= num_of_divisors:
            # exit condition
            return t

        # find triangle number at next index
        t = t + n
        n += 1


if __name__ == "__main__":
    print(naiveApproach(5))  # 28
    print(naiveApproach(23))  # 630
    # print(naiveApproach(167))  # very slow, does not give answer
    # print(naiveApproach(374))  # very slow, does not give answer
    # print(naiveApproach(500))  # very slow, does not give answer

    print(optimumSolution(5))  # 28
    print(optimumSolution(23))  # 630
    print(optimumSolution(167))  # 1385280
    print(optimumSolution(374))  # 17907120
    print(optimumSolution(500))  # 76576500
