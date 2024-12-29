from dataclasses import dataclass


@dataclass
class Node:
    y: int
    x: int
    s: int
    p: "Node | None"

    def in_grid(self):
        if self.y < 0 or self.y > h :
            return False

        if self.x < 0 or self.x > w:
            return False

        return True


directions = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1)  # left
]


def part1(corrupted: set[tuple[int, ...]]):
    to_check = [Node(0, 0, 0, None)]
    visited = {(0, 0)}

    while to_check:
        node = to_check.pop(0)

        for dy, dx in directions:
            ny, nx = node.y + dy, node.x + dx
            n = Node(ny, nx, node.s + 1, node)

            if not n.in_grid():
                continue

            if (ny, nx) in corrupted:
                continue

            if (ny, nx) in visited:
                continue

            if (ny, nx) == (h, w):
                return n.s

            visited.add((ny, nx))
            to_check.append(n)


def part2(positions: list[tuple[int, ...]]):
    corrupted, remaining = positions[:12 if test else 1024], positions[12 if test else 1024:]

    corrupted = set(corrupted)

    for py, px in remaining:
        corrupted.add((py, px))
        score = part1(corrupted)

        if score is None:
            return f"{py},{px}"

    return 0


def main():
    with open(filename) as f:
        raw = f.read()

    positions = [tuple(map(int, line.split(","))) for line in raw.splitlines()]

    print(part1(set(positions[:12 if test else 1024])))
    print(part2(positions))


if __name__ == "__main__":
    test = False
    h, w = (6, 6) if test else (70, 70)
    filename = "example.txt" if test else "input.txt"
    start = 0,0

    main()
