# https://projecteuler.net/problem=17

# Use memoization technique where we store the results of previous values in dictionary and reuse them
# https://radiusofcircle.blogspot.com/2016/04/problem-17-project-euler-solution-with-python.html
if __name__ == "__main__":
    # dictionary to store all the letter counts
    # we initialize dictionary manually from range 1-20, then 30, 40, 50, 60, 70, 80, 90
    dictionary_words = {0: 0,  # zero is does not contribute to the count
                        1: 3,  # one
                        2: 3,  # two
                        3: 5,  # three
                        4: 4,  # four
                        5: 4,  # five
                        6: 3,  # six
                        7: 5,  # seven
                        8: 5,  # eight
                        9: 4,  # nine
                        10: 3,  # ten
                        11: 6,  # eleven
                        12: 6,  # twelve
                        13: 8,  # thirteen
                        14: 8,  # fourteen
                        15: 7,  # fifteen
                        16: 7,  # sixteen
                        17: 9,  # seventeen
                        18: 8,  # eighteen
                        19: 8,  # nineteen
                        20: 6,  # twenty
                        30: 6,  # thirty
                        40: 5,  # forty
                        50: 5,  # fifty
                        60: 5,  # sixty
                        70: 7,  # seventy
                        80: 6,  # eighty
                        90: 6}  # ninety

    # we then compute values from 20 to 99
    for i in range(21, 100):
        tens_place = int(i / 10) * 10
        ones_place = i - tens_place

        dictionary_words[i] = dictionary_words[tens_place] + dictionary_words[ones_place]

    # we then compute values from 100 to 1000
    for i in range(100, 1000):

        hundreds_place = int(i / 100)
        tens_and_ones_place = i - hundreds_place * 100

        if tens_and_ones_place == 0:
            # for numbers like _00
            dictionary_words[i] = dictionary_words[hundreds_place] + 7  # 7 = hundred
        else:
            dictionary_words[i] = dictionary_words[hundreds_place] + dictionary_words[
                tens_and_ones_place] + 10  # 10 = and hundred

    dictionary_words[1000] = 11  # one thousand

    print(sum(dictionary_words.values()))
