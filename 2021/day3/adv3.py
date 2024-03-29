#!/usr/bin/env python3

from typing import List

def get_bit_count(diag_codes: List[str]):
    number_of_bits = len(diag_codes[0])
    bits_count = [0.0] * number_of_bits

    for code in diag_codes:
        bits = list(code)
        for index in range(len(bits)):
            bits_count[index] += int(bits[index])
    return bits_count


def get_rates(diag_codes: List[str]):
    bits_count = get_bit_count(diag_codes)

    number_of_codes = len(diag_codes)
    gamma_rate = ""
    epsilon_rate = ""

    for bit in bits_count:
        bit_value = bit / number_of_codes
        if bit_value > 0.5:
            gamma_rate += str(1)
            epsilon_rate += str(0)
        else:
            gamma_rate += str(0)
            epsilon_rate += str(1)

    return gamma_rate, epsilon_rate


def convert_binary(binary: str):
    return int(binary, 2)


def adv3_1(diag_codes: List[str]):
    gamma_rate, epislon_rate = get_rates(diag_codes)
    gamma_value = convert_binary(gamma_rate)
    epsilon_value = convert_binary(epislon_rate)
    print("gamma:", gamma_value, "epsilon:", epsilon_value)

    return(gamma_value * epsilon_value)


def calc_common_bits(codes: List[str], index: int, gas: str):
    one = 0
    zero = 0

    for code in codes:
        bits = list(code)
        if int(bits[index]) == 1:
            one += 1
        else:
            zero += 1

    if gas == "o2":
        if one >= zero:
            return 1
        else:
            return 0
    if gas == "co2":
        if one < zero:
            return 1
        else:
            return 0


def get_gas_rating(diag_codes: List[str], start_index: int, gas: str):
    if len(diag_codes) == 1:
        return convert_binary(diag_codes[0])
    codes_for_next = []
    most_common = calc_common_bits(diag_codes, start_index, gas)
    for code in diag_codes:
        bits = list(code)
        if int(bits[start_index]) == most_common:
            codes_for_next.append(code)
    return get_gas_rating(codes_for_next, start_index+1, gas)


def adv3_2(diag_codes: List[str]):
    o2_rating: int = get_gas_rating(diag_codes, 0, "o2")
    co2_rating: int = get_gas_rating(diag_codes, 0, "co2")
    print("o2:", o2_rating,"co2:", co2_rating)
    return o2_rating * co2_rating


def main():
    lines = []
    with open("diagnostics.txt") as f:
        lines = f.read().splitlines()
    f.close()

    print("part 1 - power consumption:", adv3_1(lines))
    print("part 2 - life support rating:", adv3_2(lines))

if __name__ == '__main__':
    main()
