from functools import lru_cache


def can_assemble_design(patterns: list[str], design: str):

    @lru_cache(maxsize=None)
    def cached(rem: str):
        if not rem:
            return True

        possible = 0
        for pattern in patterns:
            if rem.startswith(pattern):
                possible += cached(rem[len(pattern):])

        return possible

    return cached(design)


def part1(patterns: list[str], designs: list[str]):
    return sum(bool(can_assemble_design(patterns, design)) for design in designs)


def part2(patterns: list[str], designs: list[str]):
    return sum(can_assemble_design(patterns, design) for design in designs)


def main(test: bool):
    filename = "example.txt" if test else "input.txt"
    with open(filename) as f:
        raw = f.read()

    patterns, designs = raw.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()

    print(part1(patterns, designs))
    print(part2(patterns, designs))


if __name__ == "__main__":
    main(test=False)
