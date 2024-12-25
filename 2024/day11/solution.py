from functools import lru_cache

def apply_rules(stone: int):
    if stone == 0:
        return [1]
    
    if len(sstone := str(stone)) % 2 == 0:
        return [int(sstone[:len(sstone)//2]), int(sstone[len(sstone)//2:])]

    return [stone * 2024]


def part1(blinks: int):
    stones = [*map(int, raw.split()),]

    for _ in range(blinks):
        ns = [apply_rules(stone) for stone in stones]
        stones = []
        for s in ns:
            stones.extend(s)

    return len(stones)


def part2(blinks: int):
    stones = [*map(int, raw.split()),]

    for _ in range(blinks):
        ns = [apply_rules(stone) for stone in stones]
        stones = []
        for s in ns:
            stones.extend(s)
        
        print(_)

    return len(stones)


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()
    

    print(part1(25))
    print(part2(75))
