# https://projecteuler.net/problem=22


def compute_numerical_value(name):
    num = 0
    for c in name:
        num += ((ord(c) % 65) + 1)
    return num


def naiveApproach(names):
    # sort alphabetically
    # sorting is inplace in python
    names.sort()
    result = 0

    for i in range(len(names)):
        # iterate through each and then compute its numerical value
        value = compute_numerical_value(names[i])

        # multiply with its position
        result += (value * (i + 1))

    return result


if __name__ == "__main__":
    with open("p022_names.txt") as f:
        contents = f.read()
        contents = contents.replace('"', "")
        contents = contents.split(",")

    print(naiveApproach(contents))
