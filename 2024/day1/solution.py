from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()


def part1():
    left, right = [], []

    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    total_distance = 0

    for i in range(len(left)):
        dist = abs(left[i] - right[i])
        total_distance += dist

    return total_distance


def part2():
    left, right = [], defaultdict(lambda: 0)

    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right[r] += 1

    left.sort()

    similarity = 0

    for num in left:
        similarity += num * right[num]

    return similarity


if __name__ == '__main__':
    print(part2())
