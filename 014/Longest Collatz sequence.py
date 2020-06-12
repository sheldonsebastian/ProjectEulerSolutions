# https://projecteuler.net/problem=14
import time


def naiveApproach(limit):
    """Brute force method, where we iterate through all numbers below the limit and then keep track of Collatz chain
    count and then return the number with the longest chain count. This approach is slow and completes the operation
    in O(limit * longest chain count) """
    max_count = 1
    result = 1

    for num in range(1, limit):

        count = 1
        # store the num in another variable since we are altering num
        ans = num

        # collatz chain will converge to 1
        while num != 1:
            # even
            if num % 2 == 0:
                num = num // 2
            # odd
            else:
                num = 3 * num + 1

            count += 1

        # if the chain size is greater than max, then update the max with new chain count and also update the result
        # with the ans
        if count > max_count:
            max_count = count
            result = ans

    return result


def countChain(n, previous_collatz):
    """Method which recursively computes collatz chain size"""
    if previous_collatz.get(n) is not None:
        # found in dictionary
        return previous_collatz.get(n)
    else:
        # not found in dictionary, thus compute collatz chain
        if n % 2 == 0:
            # even
            previous_collatz[n] = 1 + countChain((n / 2), previous_collatz)
        else:
            # odd
            previous_collatz[n] = 2 + countChain(((3 * n + 1) / 2), previous_collatz)

    return previous_collatz[n]


# https://projecteuler.net/overview=014
def optimumSolution(limit):
    """Inefficiencies in the naiveApproach:
    1. We are recomputing collatz chain from scratch, i.e. we are not storing the results from previous iterations. Use
    memoization.

    2. For even number, collatz chain can be computed as collatz(n) = collatz(n/2) + 1, thus all numbers below n/2 will
    have collatz chain count smaller than all number above n/2, thus we need to compute from n//2 upto n

    3. For odd numbers, we are computing next number as n = (3n+1), this makes n an even number. Thus we can find the
     collatz(odd n) = collatz((3n + 1) /2) + 2. Here we add 2 since 1 is for the even number contribution to the collatz
    chain and 1 is for the original odd number contribution to the collatz chain
    """

    # dictionary to store previous collatz chain sizes, we initialize 1 with chain size of 1, since only 1 element is
    # present
    previous_collatz = {1: 1}
    max_count = 1
    result = 1

    # iterate from limit//2 upto limit
    for i in range(limit // 2, limit):

        # store the num in another variable since we are altering num
        count = countChain(i, previous_collatz)

        # if the chain size is greater than max, then update the max with new chain count and also update the result
        # with the ans
        if count > max_count:
            max_count = count
            result = i

    return result


if __name__ == "__main__":
    print(naiveApproach(14))  # 9
    print(naiveApproach(5847))  # 3711
    print(naiveApproach(46500))  # 35655
    print(naiveApproach(54512))  # 52527
    print(naiveApproach(100000))  # 77031
    # start = time.time()
    print(naiveApproach(1000000))  # 837799, took 30 seconds that is very slow
    # print(time.time() - start)

    print(optimumSolution(14))  # 9
    print(optimumSolution(5847))  # 3711
    print(optimumSolution(46500))  # 35655
    print(optimumSolution(54512))  # 52527
    print(optimumSolution(100000))  # 77031
    # start = time.time()
    print(optimumSolution(1000000))  # 837799, took 1 second, BOOM that is faster than naive approach
    # print(time.time() - start)
