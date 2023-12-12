#!/usr/bin/python3


def to_subtract(list_number):
    to_sub = 0
    max_list = max(list_number)

    for a in list_number:
        if max_list > a:
            to_sub += a

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_key = list(rom_num.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for ch in roman_string:
        for r_num in list_key:
            if r_num == ch:
                if rom_num.get(ch) <= last_roman:
                    number += to_subtract(list_number)
                    list_number = [rom_num.get(ch)]
                else:
                    list_number.append(rom_num.get(ch))

                last_roman = rom_num.get(ch)

    number += to_subtract(list_number)

    return (number)
