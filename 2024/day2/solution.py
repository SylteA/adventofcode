def validate(digits: list[int]) -> int:
    incremental = digits[0] < digits[1]

    for i in range(len(digits) - 1):
        a, b = digits[i], digits[i + 1]

        if a == b:
            return i

        if abs(a - b) > 3:
            return i

        if a > b and incremental:
            return i
        elif b > a and not incremental:
            return i

    return -1


def part1():
    safe = 0

    for line in lines:
        digits = [*map(int, line.split())]

        if validate(digits) == -1:
            safe += 1

    return safe


def part2():
    safe = 0

    for line in lines:
        digits = list(map(int, line.split()))

        if validate(digits) == -1:
            safe += 1
            continue

        for i in range(len(digits)):
            modified = digits[:i] + digits[i + 1:]

            if validate(modified) == -1:
                safe += 1
                break

    return safe


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    print(part2())
