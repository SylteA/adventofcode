import math
import string

non_symbols = {*string.digits, "."}


def part1():
    numbers = []

    for i in len(lines):
        for j in len(lines[0]):


    return sum(numbers)


def part2():
    return


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(part1())
    print(part2())
