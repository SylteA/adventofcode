from collections import defaultdict
from itertools import combinations


def in_grid(y: int, x: int):
    if y < 0 or y > height - 1:
        return False
    
    if x < 0 or x > width - 1:
        return False
    
    return True


def format_grid(g):
    return "\n".join("".join(row) for row in g)


def part1():
    for _, positions in antennas.items():
        for (y0, x0), (y1, x1) in combinations(positions, 2):
            oy, ox = y1 - y0, x1 - x0

            if in_grid(y0 - oy, x0 - ox):
                grid[y0 - oy][x0 - ox] = "#"

            if in_grid(y1 + oy, x1 + ox):
                grid[y1 + oy][x1 + ox] = "#"

    fmt = format_grid(grid)
    return fmt.count("#")


def part2():
    for _, positions in antennas.items():
        for (y0, x0), (y1, x1) in combinations(positions, 2):
            oy, ox = y1 - y0, x1 - x0

            while True:
                y0, x0 = y0 - oy, x0 - ox
                if not in_grid(y0, x0):
                    break

                if grid[y0][x0] != ".":
                    continue

                grid[y0][x0] = "#"

            while True:
                y1, x1 = y1 + oy, x1 + ox
                if not in_grid(y1, x1):
                    break

                if grid[y1][x1] != ".":
                    continue

                grid[y1][x1] = "#"


    fmt = format_grid(grid)
    return fmt.count("#") + sum(fmt.count(char) for char in antennas.keys())


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()
        grid = [[*line] for line in raw.splitlines()]

    height, width = len(grid), len(grid[0])
    antennas: dict[str, set[tuple[int, int]]] = defaultdict(set)

    for y in range(height):
        for x in range(width):
            if grid[y][x] == ".":
                continue

            antennas[grid[y][x]].add((y, x))

    print(part1())
    print(part2())
