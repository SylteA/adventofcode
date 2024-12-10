from collections import defaultdict


def breaks_rules(page: list[int]):
    c = page[0]

    if c not in rules:
        return False

    for r in rules[c]:
        if r in page[1:]:
            return True

    return False


def part1():
    global invalid_pages
    middles = []

    for page in pages:
        page = page[::-1]

        valid = True

        for i in range(len(page)):
            if breaks_rules(page[i:]):
                valid = False
                invalid_pages.append(page[::-1])
                break

        if valid:
            middles.append(page[int(len(page) / 2)])

    return sum(middles)


def part2():
    middles = []

    for page in invalid_pages:
        l, r = 0, 1
        while r < len(page):
            if page[l] in rules[page[r]]:
                page[l], page[r] = page[r], page[l]

            r += 1
            if r == len(page):
                l += 1
                r = l + 1

        middles.append(page[len(page) // 2])

    return sum(middles)


def parse_data(file):
    with open(file) as f:
        data = f.read()

    raw_rules, raw_pages = data.split("\n\n")
    p = [[int(num) for num in page.split(",")] for page in raw_pages.splitlines()]

    r = defaultdict(set)
    for rule in raw_rules.splitlines():
        a, b = map(int, rule.split("|"))
        r[a].add(b)

    return p, r


if __name__ == '__main__':
    pages, rules = parse_data("input.txt")
    invalid_pages = []

    print(part1())
    print(part2())
