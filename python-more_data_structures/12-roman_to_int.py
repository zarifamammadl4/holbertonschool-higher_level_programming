#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""

    if roman_string is None or type(roman_string) is not str:
        return 0

    roman = {
        I: 1, V: 5, X: 10, L: 50,
        C: 100, D: 500, M: 1000
    }

    total = 0
    i = 0
    length = len(roman_string)

    while i < length:
        # current value
        s1 = roman.get(roman_string[i], 0)

        # look ahead
        if i + 1 < length:
            s2 = roman.get(roman_string[i + 1], 0)

            # subtraction case
            if s1 < s2:
                total += (s2 - s1)
                i += 2
                continue

        # normal add
        total += s1
        i += 1

    return total
