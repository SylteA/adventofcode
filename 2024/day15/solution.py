actions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


def part1(grid: list[list[str]]):
    height, width = len(grid), len(grid[0])
    ry, rx = find_index_of(grid, "@")
    grid[ry][rx] = "."

    for move in movements:
        dy, dx = actions[move]
        if grid[ry + dy][rx + dx] == '#':
            continue
        elif grid[ry + dy][rx + dx] == '.':
            ry, rx = ry + dy, rx + dx
            continue

        for i in range(2, height):
            if grid[ry + dy * i][rx + dx * i] == "#":
                break

            if grid[ry + dy * i][rx + dx * i] == ".":
                grid[ry + dy * i][rx + dx * i] = 'O'
                grid[ry + dy][rx + dx] = "."
                ry, rx = ry + dy, rx + dx
                break

    return score(grid, "O")


def part2(grid: list[list[str]]):
    height, width = len(grid), len(grid[0])
    ry, rx = find_index_of(grid, "@")
    grid[ry][rx] = "."

    for move in movements:
        dy, dx = actions[move]
        if grid[ry + dy][rx + dx] == '#':
            continue
        if grid[ry + dy][rx + dx] == '.':
            ry, rx = ry + dy, rx + dx
            continue

        if move in ("<", ">"):
            for i in range(2, width):
                if grid[ry][rx + dx * i] == "#":
                    break

                if grid[ry][rx + dx * i] == ".":
                    grid[ry].pop(rx + dx * i)
                    grid[ry].insert(rx, ".")
                    rx = rx + dx
                    break
        else:
            to_check = {(ry + dy, rx)}
            to_move = set()
            while to_check:
                ny, nx = to_check.pop()
                if (ny, nx) in to_move:
                    continue
                to_move.add((ny, nx))
                if grid[ny][nx] == "#":
                    to_check, to_move = set(), set()
                elif grid[ny][nx] == "[":
                    to_check.add((ny, nx + 1))
                    to_check.add((ny + dy, nx))
                elif grid[ny][nx] == "]":
                    to_check.add((ny, nx - 1))
                    to_check.add((ny + dy, nx))
                else:
                    to_move.remove((ny, nx))

            for ny, nx in sorted(to_move, key=lambda b: b[0])[::-dy]:
                grid[ny + dy][nx], grid[ny][nx] = grid[ny][nx], grid[ny + dy][nx]

            if to_move:
                ry, rx = ry + dy, rx + dx

    return score(grid, "[")


def parse_grid(grid: str) -> list[list[str]]:
    return [[*line] for line in grid.splitlines()]


def score(grid, target):
    total = 0

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != target:
                continue

            total += 100 * y + x

    return total


def find_index_of(grid, target):
    for y, row in enumerate(grid):
        if target in row:
            return y, row.index(target)
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()

    grd, movements, *_ = raw.split("\n\n")
    movements = movements.replace("\n", "")

    print(part1(parse_grid(grd)))

    grd = (
        grd
        .replace("#", "##")
        .replace(".", "..")
        .replace("O", "[]")
        .replace("@", "@.")
    )

    print(part2(parse_grid(grd)))
