import re


def part1():
    values = []

    for line in lines:
        digits = []

        for char in line:
            if char.isdigit():
                digits.append(char)

        first, last = digits[0], digits[-1]
        values.append(int(first + last))

    return sum(values)


def part2():
    values = []
    nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in lines:
        digits = []

        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            else:
                for num in nums.keys():
                    if line[i:].startswith(num):
                        digits.append(nums[num])

        first, last = digits[0], digits[-1]
        values.append(int(first + last))

    return sum(values)

if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()

    print(part1())
    print(part2())
