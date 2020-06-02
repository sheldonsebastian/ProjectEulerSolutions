# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
# https://projecteuler.net/problem=3
import math


def get_prime_numbers(limit):
    """To generate prime numbers less than and equal to 'limit' we use Sieve of Eratosthenes algorithm O(n*log(log(n))).
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/ """

    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    prime = [True for _ in range(0, limit + 1)]

    # we find prime numbers starting from 2
    p = 2

    # The reasoning for using p*p ==> https://math.stackexchange.com/questions/1514568/sieve-of-eratosthenes-refinement
    while p * p <= limit:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p (thus increment the for loop by p) starting from p*p upto and including n
            for i in range(p * p, limit + 1, p):
                prime[i] = False

        # find the next prime number by incrementing variable by 1
        p += 1

    # return all numbers whose value is True in the list
    return [p for p in range(2, limit + 1) if prime[p]]


def naiveApproach(num):
    """here the issue is that we need to generate a list of prime numbers upto num"""

    # generate ascending list of prime numbers upto num
    prime_numbers = get_prime_numbers(num)

    for prime in prime_numbers:
        # if remainder of num with prime number is 0, then keep dividing the num, else increment the prime number
        while num % prime == 0:
            num /= prime

        if num == 1:
            # once the num cannot be divided anymore i.e. num=1, whatever is the prime number which divided it last
            # is the max prime number
            return prime


# https://medium.com/@TheZaki/project-euler-3-largest-prime-factor-92ec4f46ce3b
def optimumSolution(num):
    """Here we overcome the slowness of naiveApproach, by finding prime numbers only upto sqrt(num). Since for any
    composite number 'num' we can have maximum 1 prime number greater than sqrt(num). Thus when we divide the num by
    the prime factors upto sqrt(num) we will get the largest prime factor in the prime factor list(from our
    get_prime_numbers function) or the quotient of the division with num will be the largest prime factor itself """

    # generate ascending list of prime numbers upto num
    prime_numbers = get_prime_numbers(math.floor(math.sqrt(num)) + 1)

    for prime in prime_numbers:
        # if remainder of num with prime number is 0, then keep dividing the num, else increment the prime number
        while num % prime == 0:
            num //= prime

        if num == 1:
            # once the num cannot be divided anymore i.e. num=1, whatever is the prime number which divided it last
            # is the max prime number
            return prime

    return num


if __name__ == "__main__":
    print(naiveApproach(2))  # 2
    print(naiveApproach(3))  # 3
    print(naiveApproach(5))  # 5
    print(naiveApproach(7))  # 7
    print(naiveApproach(8))  # 2
    print(naiveApproach(23))  # 23
    print(naiveApproach(33))  # 11
    print(naiveApproach(13195))  # 29
    # print(naiveApproach(600851475143))  # timed out, cannot find solution need to find better approach

    print()
    print(optimumSolution(2))  # 2
    print(optimumSolution(3))  # 3
    print(optimumSolution(5))  # 5
    print(optimumSolution(7))  # 7
    print(optimumSolution(8))  # 2
    print(optimumSolution(23))  # 23
    print(optimumSolution(33))  # 11
    print(optimumSolution(13195))  # 29
    print(optimumSolution(600851475143))  # 6857 and wow that was fast
