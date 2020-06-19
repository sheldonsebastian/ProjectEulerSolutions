# https://projecteuler.net/problem=19


if __name__ == "__main__":
    # we want to find number of Sundays from 1st January 1901 to 31st December 2001 which lie on 1st of every month
    result = 0

    # 0 = Sunday, 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5= Friday,  6 = Saturday
    dow = 2  # 1st January 1901 is tuesday

    # Jan, Feb, Mar, ...., Dec
    months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for year in range(1901, 2001):
        months[1] = 28 + (1 if (year % 4 == 0 and year % 100 != 00 or year % 400 == 0) else 0)

        for month in months:
            # add the month and check if it is Sunday or not
            dow = (dow + month) % 7

            if dow == 0:
                result += 1

    print(result)  # 171 Sundays lie on 1st of every month
