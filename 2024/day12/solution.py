
directions = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),   # down
    (0, -1)    # left
]


def in_grid(y: int, x: int):
    if y < 0 or y > height - 1:
        return False

    if x < 0 or x > width - 1:
        return False

    return True


def find_areas():
    searched = {}  # type: dict[(int, int), bool]
    areas = []

    for y in range(width):
        for x in range(height):
            if (y, x) in searched:
                continue

            area = search_area(y, x)
            searched |= area
            areas.append(area)

    return areas


def search_area(y, x):
    coordinates = {}
    to_search = [(y, x)]
    target = grid[y][x]

    while to_search:
        y, x = to_search.pop()

        if (y, x) in coordinates:
            continue

        coordinates[(y, x)] = grid[y][x]
        for dy, dx in directions:
            if not in_grid(y+dy, x+dx):
                continue

            if grid[y+dy][x+dx] == target:
                to_search.append((y + dy, x + dx))

    return coordinates


def get_perimeter(area):
    perimeter = 0

    for y, x in area.keys():
        target = grid[y][x]
        for dy, dx in directions:
            point = get_point(y+dy, x+dx)
            perimeter += point != target

    return perimeter

def get_point(y, x):
    if not in_grid(y, x):
        return None

    return grid[y][x]


def count_corners(area):
    outside, inside = 0, 0

    for y, x in area.keys():
        target = grid[y][x]

        up = get_point(y+1, x)
        right = get_point(y, x+1)
        up_right = get_point(y+1, x+1)
        down_right = get_point(y-1, x+1)
        down = get_point(y-1, x)
        down_left = get_point(y-1, x-1)
        left = get_point(y, x-1)
        up_left = get_point(y+1, x-1)

        if target not in (up, right, up_right):
            outside += 1

        if target not in (down, right, down_right):
            outside += 1

        if target not in (up, left, up_left):
            outside += 1

        if target not in (down, left, down_left):
            outside += 1

        if down != target and down_left == target:
            inside += 1

        if up != target and up_left == target:
            inside += 1

        if down != target and down_right == target:
            inside += 1

        if up != target and up_right == target:
            inside += 1

    return outside + inside


def part1():
    areas = find_areas()

    price = 0
    for area in areas:
        size = len(area)
        perimeter = get_perimeter(area)
        price += size * perimeter

    return price


def part2():
    areas = find_areas()

    price = 0
    for area in areas:
        size = len(area)
        corners = count_corners(area)
        price += size * corners

    return price


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()
        grid = [[*line] for line in raw.splitlines()]

    height, width = len(grid), len(grid[0])

    print(part1())
    print(part2())
