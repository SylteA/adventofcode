from dataclasses import dataclass
import typing as t


@dataclass
class Node:
    y: int
    x: int
    d: int
    s: int
    p: t.Optional["Node"]


directions = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1)  # left
]


def part1(grid: list[list[str]]):
    y, x = locate(grid, "S")

    to_check = [Node(y, x, 1, 0, None)]
    nodes = {(y, x): to_check[0]}
    paths = []

    while to_check:
        node = to_check.pop(0)

        possible_moves = [
            (node.d, node.s + 1),
            ((node.d - 1) % 4, node.s + 1001),
            ((node.d + 1) % 4, node.s + 1001),
        ]

        for direction, score in possible_moves:
            dy, dx = directions[direction]
            ny, nx = node.y + dy, node.x + dx

            n = Node(ny, nx, direction, score, node)

            if grid[ny][nx] == "#":
                continue

            if (ny, nx) in nodes and nodes[(ny, nx)].s + 1000 < score:
                continue

            if grid[ny][nx] == "E":
                paths.append(n)

            nodes[(ny, nx)] = n
            to_check.append(n)

    return paths


def part2(paths: list[Node]):
    visited = set()

    for path in paths:
        while path.p is not None:
            visited.add((path.y, path.x))
            path = path.p

    return len(visited) + 1


def locate(grid, target):
    for y, row in enumerate(grid):
        if target in row:
            return y, row.index(target)
    return None


def main():
    with open("input.txt") as f:
        raw = f.read()

    grid = [[*line] for line in raw.splitlines()]

    paths = part1(grid)
    shortest = min(paths, key=lambda p: p.s)
    paths = [path for path in paths if path.s == shortest.s]

    print(shortest.s)
    print(part2(paths))


if __name__ == "__main__":
    main()
