# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
# https://projecteuler.net/problem=3


def naiveApproach(num):
    # 20 = 2 x 2 x 5
    # iterate through list of prime numbers
    # if remainder of num with prime number is 0, then keep dividing the num, else increment the prime number
    # repeat this till prime number < num

    # here the issue is that we need to generate a list of prime numbers upto num which maybe a slow process
    pass


def optimumSolution(num):
    # https://projecteuler.net/overview=003
    # every number n can at most(maximum) have one prime factor greater than sqrt(n)

    pass


if __name__ == "__main__":
    print(naiveApproach(2))
    print(naiveApproach(3))
    print(naiveApproach(5))
    print(naiveApproach(7))
    print(naiveApproach(8))
    print(naiveApproach(13195))
    print(naiveApproach(600851475143))
