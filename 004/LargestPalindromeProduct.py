# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers. In general,
# find the largest palindrome made from the product of two n-digit numbers.


def check_palindrome(n):
    n_string = str(n)

    if n_string[::] == n_string[-1::-1]:
        return True
    else:
        return False


def naiveApproach(ndigit):
    # naive approach eg: for 2 digit, the largest number is 99. Thus store products of 99 with all combinations from
    # 99 to 10 and then check which product is the maximum palindrome.
    largest_num = int("9" * ndigit)
    smallest_num = int("1" + "0" * (ndigit - 1)) - 1
    max_product = -1
    for i in range(largest_num, smallest_num, -1):
        for j in range(largest_num, smallest_num, -1):
            if check_palindrome(i * j):
                if max_product < (i * j):
                    max_product = i * j

    # issue here is that the time complexity to find the largest palindrome will be O(10^2n) which is exponential and
    # very very very bad solution.
    return max_product


# https://projecteuler.net/overview=004
def optimumSolution(ndigit):
    """ abccba = 11(9091a+910b+100c), thus one of the two factors for the largest palindrome product should be
    multiple of 11. This is true for all palindrome product containing ndigit factors"""

    # max palindrome product
    max_product = -1

    # largest number using ndigit
    largest_num = int("9" * ndigit)

    # smallest number using ndigit
    smallest_num = int("1" + "0" * (ndigit - 1))

    # we will find the palindrome products, by iterating in descending order for factor1 and factor2
    factor1 = largest_num
    while factor1 >= smallest_num:

        # either factor1 could be multiple of 11
        if factor1 % 11 == 0:

            # if factor1 is multiple of 11, then initialize factor2 to be largest_number
            factor2 = largest_num

            # and decrement factor2 by steps of 1
            decrease_by = 1
        else:
            # or factor2 could be multiple of 11 if factor2 is multiple of 11 then initialize it to biggest number
            # divisible by 11 and in the specified range i.e. less than largest_number
            factor2 = (largest_num // 11) * 11

            # and decrement factor2 by steps of 11
            decrease_by = 11

        # this statement avoids us to compute factor1*factor2 and factor2*factor1, thus reducing computations by half
        while factor2 >= factor1:
            # since we are generating palindromes in descending order, any palindrome number less than the
            # max_product, implies that max_product is the largest palindrome
            if factor1 * factor2 <= max_product:
                break

            if check_palindrome(factor1 * factor2):
                max_product = factor1 * factor2

            factor2 = factor2 - decrease_by

        # decrement factor by 1
        factor1 = factor1 - 1

    return max_product


if __name__ == "__main__":
    print(naiveApproach(2))
    print(naiveApproach(3))

    # start = datetime.now()
    # print(naiveApproach(4))  # takes too long ==> 59 seconds
    # print(datetime.now() - start)

    print()
    print(optimumSolution(2))
    print(optimumSolution(3))

    # start = datetime.now()
    print(optimumSolution(4))  # is faster ==> 3 ms, woah!!
    # print(datetime.now() - start)
    print(optimumSolution(2))
