import math


def part1():
    limits = {
        "red": 12,
        "blue": 14,
        "green": 13
    }

    possible_games = []

    for line in lines:
        game_id, subsets = line.split(":")
        game_id = game_id.lstrip("Game ")
        subsets = subsets.split("; ")

        if all(
                all(int(entry.split()[0]) <= limits[entry.split()[1]] for entry in subset.split(", "))
                for subset in subsets
        ):
            possible_games.append(game_id)

    return sum(map(int, possible_games))


def part2():
    powers = []

    for line in lines:
        subsets = line[line.index(":")+2:].split("; ")
        maxes = {}

        for subset in subsets:
            for entry in subset.split(", "):
                qty, color = entry.split()
                maxes[color] = max(int(qty), maxes.get(color, 0))

        powers.append(math.prod(maxes.values()))

    return sum(powers)


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(part1())
    print(part2())
