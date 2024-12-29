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


def part1():
    y, x = locate("S")

    to_check = [Node(y, x, 1, 0, None)]
    nodes = {(y, x): to_check[0]}

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

            if grid[ny][nx] == "E":
                print("REACHED END!", n.s)

            if grid[ny][nx] == "#":
                continue

            if (ny, nx) in nodes and nodes[(ny, nx)].s < score:
                continue

            nodes[(ny, nx)] = n
            to_check.append(n)

    return nodes


def part2():
    tiles = 543

    return tiles


def parse_grid(string: str) -> list[list[str]]:
    return [[*line] for line in string.splitlines()]


def locate(target):
    for y, row in enumerate(grid):
        if target in row:
            return y, row.index(target)
    return None


if __name__ == "__main__":
    with open("example.txt") as f:
        raw = f.read()

    grid = parse_grid(raw)
    height, width = len(grid), len(grid[0])

    scores = part1()
    print(scores[locate("E")].s)
    print(part2())
