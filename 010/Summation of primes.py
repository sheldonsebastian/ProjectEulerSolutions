# https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million. To
# generalize find the sum of primes below n.


def getPrimes(limit):
    # initialize flag where all the values are set to true and size equals to limit+1 since we want inclusive primes
    number_flag = [True for _ in range(limit + 1)]

    # initialize p = 2 since 1 is composite number
    p = 2

    # we are searching till sqrt of n since any composite number will have maximum 1 prime number above sqrt of n.
    # Here we have used square of p, but it is equivalent to previous statement.
    while p * p < limit:

        # check if the number is flagged or not
        if number_flag[p]:

            # we start from p*p since all the numbers below p*p have composite numbers less than p. Similar to above
            # statement
            for x in range(p * p, limit + 1, p):
                # set all the multiples of the value to be False, since they are composite numbers which are multiple
                # of p
                number_flag[x] = False

        # increment p
        p += 1

    # return primes from 2
    return [x for x in range(2, limit + 1) if number_flag[x]]


def naiveApproach(limit):
    """We can sieve of Eratosthenes to find all the prime numbers below the limit and then sum the value."""
    return sum(getPrimes(limit))


if __name__ == "__main__":
    print(naiveApproach(10))  # 17
    print(naiveApproach(17))  # 41
    print(naiveApproach(2001))  # 277050
    print(naiveApproach(140759))  # 873608362
    print(naiveApproach(2000000))  # 142913828922
