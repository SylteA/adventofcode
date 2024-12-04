import re

with open("input.txt", "r") as f:
    memory = f.read()


def part1():
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(memory)

    total = 0

    for a, b in matches:
        total += int(a) * int(b)

    return total


def part2():
    pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(|don)")
    matches = pattern.findall(memory)

    capture = True
    total = 0

    for a, b, action in matches:
        if action == "don":
            capture = False
        elif action == "do(":
            capture = True
        else:
            if capture:
                total += int(a) * int(b)

    return total


if __name__ == '__main__':
    print(part2())
