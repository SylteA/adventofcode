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
    valid_pages = []

    for page in pages:
        page = page[::-1]

        valid = True

        for i in range(len(page)):
            if breaks_rules(page[i:]):
                valid = False
                break

        if valid:
            valid_pages.append(page[int(len(page) / 2)])

    return sum(valid_pages)


def part2():
    valid_pages = []

    for page in pages:
        page = page[::-1]

        for i in range(len(page)):
            for rule in rules[page[i]]:
                if rule in page[i:]:


    return sum(valid_pages)


def parse_data(file):
    with open(file) as f:
        data = f.read()

    raw_rules, raw_pages = data.split("\n\n")
    p = [[int(num) for num in page.split(",")] for page in raw_pages.splitlines()]

    r = defaultdict(list)
    for rule in raw_rules.splitlines():
        a, b = map(int, rule.split("|"))
        r[a].append(b)

    return p, r


if __name__ == '__main__':
    pages, rules = parse_data("example.txt")

    print(part1())
    print(part2())
