
def part1():
    def search(word: str) -> int:
        count = 0

        search_range = range(len(word))

        for row in range(len(lines)):
            for col in range(len(lines[0])):

                # Straight
                if all(lines[row][col + i] == word[i] for i in search_range):
                    count += 1

                # Down
                if all(lines[row + i][col] == word[i] for i in search_range):
                    count += 1

                # Diagonal down
                if all(lines[row + i][col + i] == word[i] for i in search_range):
                    count += 1

                # Diagonal up
                if all(lines[row - i][col + i] == word[i] for i in search_range):
                    count += 1

        return count

    return search("XMAS") + search("SAMX")


def part2():
    # Search based on the centre of the X, "A"

    count = 0

    for row in range(len(lines) - 2):
        for col in range(len(lines[0]) - 2):
            a = lines[row + 1][col + 1]

            if a != "A":
                continue

            tl, tr = lines[row][col], lines[row][col + 2]
            bl, br = lines[row + 2][col], lines[row + 2][col + 2]

            if "A" in [tl, tr, bl, br]:
                continue

            if "X" in [tl, tr, bl, br]:
                continue

            if tl == br or tr == bl:
                continue

            count += 1


    return count



if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().splitlines()

    print(part2())
