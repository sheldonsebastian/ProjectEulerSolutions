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


if __name__ == "__main__":
    print(naiveApproach(2))
    print(naiveApproach(3))
