# Find the sum of all the even-valued terms in the Fibonacci sequence
# which do not exceed four million.
# https://projecteuler.net/problem=2


def sumEvenFibonacci(num):
    a = 1
    b = 1
    sum_even = 0

    while b < num:
        if b % 2 == 0:
            sum_even += b

        temp = a
        a = b
        b = temp + b

    return sum_even


if __name__ == "__main__":
    print(sumEvenFibonacci(10))  # 10
    print(sumEvenFibonacci(60))  # 44
    print(sumEvenFibonacci(1000))  # 798
    print(sumEvenFibonacci(100000))  # 60696
    print(sumEvenFibonacci(4000000))  # 4613732
