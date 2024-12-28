
def add(a, b): return a + b
def mul(a, b): return a * b
def concat(a, b): return int(f"{a}{b}")


def recursive_solve(total, nums, ops):
    if len(nums) == 2:
        if total in [op(nums[0], nums[1]) for op in ops]:
            return total
        else:
            return 0

    a, b, *rest = nums

    for op in ops:
        if recursive_solve(total, [op(a, b), *rest], ops):
            return total

    return 0


def part1():
    totals = []

    for line in lines:
        total, numbers = line.split(": ")
        total = int(total)
        numbers = [*map(int, numbers.split())]

        totals.append(recursive_solve(total, numbers, [add, mul]))

    return sum(totals)


def part2():
    totals = []

    for line in lines:
        total, numbers = line.split(": ")
        total = int(total)
        numbers = [*map(int, numbers.split())]
        
        totals.append(recursive_solve(total, numbers, [add, mul, concat]))

    return sum(totals)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(part1())
    print(part2())
