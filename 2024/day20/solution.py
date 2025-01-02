from collections import Counter
from dataclasses import dataclass


@dataclass
class Node:
    y: int
    x: int
    d: int
    p: "Node | None"


directions = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1)  # left
]


def part1(grid: list[list[str]]):
    height, width = len(grid), len(grid[0])
    sy, sx = find_index_of(grid, "S")
    ey, ex = find_index_of(grid, "E")

    to_check = [Node(sy, sx, 0, None)]
    visited = {(sy, sx): 0}

    while to_check:
        node = to_check.pop(0)

        for dy, dx in directions:
            ny, nx = node.y + dy, node.x + dx
            n = Node(ny, nx, node.d + 1, node)

            if (ny, nx) in visited:
                continue

            if grid[ny][nx] == '#':
                break

            visited[ny, nx] = n.d

            if (ny, nx) == (ey, ex):
                return n.d

            to_check.append(n)

    saved = 0

    for (y, x), pt in visited.items():
        for dy, dx in directions:
            py, px = y + (dy * 2), x + (dx * 2)

            z = visited.get((py, px), 0) - pt
            if z > 9:
                saved += 1

    return saved


def part2(grid: list[list[str]]):
    height, width = len(grid), len(grid[0])
    # ry, rx = find_index_of(grid, "@")

    return 0


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))

    print("-" * len(row))


def parse_grid(grid: str) -> list[list[str]]:
    return [[*line] for line in grid.splitlines()]


def find_index_of(grid, target):
    for y, row in enumerate(grid):
        if target in row:
            return y, row.index(target)


def main(test: bool):
    filename = "example.txt" if test else "input.txt"
    with open(filename) as f:
        raw = f.read()

    grid = parse_grid(raw)

    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main(test=True)
