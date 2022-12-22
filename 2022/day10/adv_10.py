#!/usr/bin/env python3

from typing import List


def check_cycle(cycle: int, register_X: int, signal_strengths: List[int]) -> None:
    if (cycle - 20) % 40 == 0:
            signal_strengths.append(cycle * register_X)


def adv10_1(cycle_data: List[str]) -> int:
    cycle = 1
    register_X = 1
    signal_strenghts: List[int] = []
    for data in cycle_data:
        check_cycle(cycle, register_X, signal_strenghts)
        if data != "noop":
            cycle += 1
            check_cycle(cycle, register_X, signal_strenghts)
            _, value = data.split(" ")
            register_X += int(value)
        cycle += 1

    return sum(signal_strenghts)


def adv10_2():
    return


def main():

    cycle_data: List[str] = []
    with open("cycle_data.txt") as f:
        cycle_data = f.read().splitlines()
    f.close()

    print("part 1 - Sum of the six signal strengths:", adv10_1(cycle_data))
    print("part 2 - :", adv10_2())

if __name__ == '__main__':
    main()
