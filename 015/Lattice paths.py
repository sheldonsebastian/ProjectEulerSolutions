# https://projecteuler.net/problem=15
from solutions.approach1 import recursive_approach
from solutions.approach2 import memoized_recursive_approach
from solutions.approach3 import dynamic_programming
from solutions.approach4 import optimumSolution

if __name__ == "__main__":
    print(recursive_approach(2, 2))  # 6
    print(recursive_approach(4, 4))  # 70
    print(recursive_approach(9, 9))  # 48620
    # print(recursive_approach(20, 20))  # Too slow, no result
    print()

    print(memoized_recursive_approach(2, 2))  # 6
    print(memoized_recursive_approach(4, 4))  # 70
    print(memoized_recursive_approach(9, 9))  # 48620
    print(memoized_recursive_approach(20, 20))  # 137846528820
    print()

    print(dynamic_programming(2, 2))  # 6
    print(dynamic_programming(4, 4))  # 70
    print(dynamic_programming(9, 9))  # 48620
    print(dynamic_programming(20, 20))  # 137846528820
    print()
