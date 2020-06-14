# https://projecteuler.net/problem=16


def naiveApproach(exponent):
    # python handles big numbers natively, :-P
    return sum(map(int, str(2 ** exponent)))


if __name__ == "__main__":
    print(naiveApproach(1000))  # 1366
