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


def get_divisors_count(number):
    exponents = []
    exponent_value = 0
    while number % 2 == 0:
        number //= 2
        exponent_value += 1

    if exponent_value != 0:
        exponents.append(exponent_value)

    # number must be odd at this point so a skip of 2 ( i = i + 2) can be used, go only till sqrt of number since any
    # composite number will have atmost one prime number above its square root
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        exponent_value = 0

        # while i divides n , print i ad divide n
        while number % i == 0:
            number = number // i
            exponent_value += 1

        if exponent_value != 0:
            exponents.append(exponent_value)

    count = 1
    for exponent in exponents:
        count *= (exponent + 1)

    return count


# https://projecteuler.net/overview=012
def optimumSolution(num_of_divisors):
    """We can find all the prime factors of a triangle number in the form of p1^a * p2^b * p3^c * ... =
    triangle_number. Then we can find the number of divisors of a triangle number by (a+1)*(b+1)*(c+1)... This works
    because we are finding all combination of exponent numbers starting from 0 (that is why we added 1) upto the
    exponent value itself. Also any triangle number at index n can be written as t = (n*(n+1))/2. Thus we can find
    the corresponding number of divisors for n and (n+1)/2 and then multiply them to get the total number of divisors
    for triangle number t """

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
