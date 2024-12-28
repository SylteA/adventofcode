from collections import defaultdict


actions = {
    0: (-1, 0),  # up
    1: (0, 1),  # right
    2: (1, 0),   # down
    3: (0, -1)    # left
}


def in_grid(y: int, x: int):
    if y < 0 or y > height - 1:
        return False
    
    if x < 0 or x > width - 1:
        return False
    
    return True

def walk_grid():
    mygrid = grid.copy()
    rotations = 0

    y, x = divmod(idx, height)
    change = actions[rotations % 4]

    while True:
        next_y = y + change[0]
        next_x = x + change[1]

        if not in_grid(next_y, next_x):
            mygrid[y][x] = "X"
            break

        if mygrid[next_y][next_x] == "#":
            rotations += 1
            change = actions[rotations % 4]
            next_y = y + change[0]
            next_x = x + change[1]

        mygrid[y][x] = "X"
        y, x = next_y, next_x

    return mygrid


def part1():
    mygrid = walk_grid()
    fmt = format_grid(mygrid)
    return fmt.count("X")


def part2():
    default = walk_grid()

    looped_replacements = 0

    for def_y in range(len(default)):
        for def_x in range(len(default[def_y])):
            mygrid = grid.copy() 

            if default[def_y][def_x] == ".":
                continue

            if default[def_y][def_x] == "^":
                continue

            mygrid[def_y][def_x] = "#"
            rotations = 0

            y, x = divmod(idx, height)
            change = actions[rotations % 4]
            visited: dict[tuple[int, int], set[int]] = defaultdict(set)

            while True:
                next_y = y + change[0]
                next_x = x + change[1]
                next_pos = (next_y, next_x)

                if not in_grid(next_y, next_x):
                    break

                if next_pos in visited:
                    if rotations % 4 in visited[next_pos]:
                        looped_replacements += 1
                        print(def_y, def_x, default[def_y][def_x], "                             LOOPED")
                        break

                visited[(next_y, next_x)].add(rotations % 4)

                if mygrid[next_y][next_x] == "#":
                    rotations += 1
                    change = actions[rotations % 4]
                    next_y = y + change[0]
                    next_x = x + change[1]

                # mygrid[y][x] = "X"
                y, x = next_y, next_x

    return looped_replacements


def format_grid(g):
    return "\n".join("".join(row) for row in g)


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()
        grid = [[*line] for line in raw.splitlines()]

    height, width = len(grid), len(grid[0])
    idx = raw.replace("\n","").index("^")

    print(part1())
    print(part2())
