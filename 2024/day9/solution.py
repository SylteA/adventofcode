from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Block:
    file_id: int
    pos: int
    data: str


def parse_blocks():
    blocks = []  # type: list[Block]
    pos = 0

    for i in range(0, len(data), 2):
        for _ in range(int(data[i])):
            blocks.append(Block(i//2, pos, str(i//2)))
            pos += 1

        if i == len(data) - 1:
            break

        for _ in range(int(data[i+1])):
            blocks.append(Block(-(i//2)-1, pos, "."))
            pos += 1
    
    return blocks


def part1():
    l, r = 0, len(blocks) - 1
    
    while l < r:
        if blocks[l].data != ".":
            l += 1
            continue
        
        if blocks[r].data == ".":
            r -= 1
            continue

        blocks[l], blocks[r] = blocks[r], blocks[l]

    s = 0
    i = 0

    for i, b in enumerate(blocks):
        if b.data == ".": continue
        s += i * b.file_id

    return s

def print_blocksystem(blocks: list[Block], prefix = " "):
    print(prefix, end="")
    for block in blocks:
        print(block.data, end="")
    print()


def part2():
    blocks = parse_blocks()
    print_blocksystem(blocks)

    l, r = 0, len(blocks) - 1
    
    file_sizes = defaultdict(int)
    for b in blocks:
        file_sizes[b.file_id] += 1

    while l < r:
        print(l, blocks[l], )
        if blocks[l].data != ".":
            l += 1
            continue
        
        if blocks[r].data == ".":
            r -= 1
            continue

        if file_sizes[blocks[l].file_id] < file_sizes[blocks[r].file_id]:
            # print("L is smaller than R", l, r)
            # print("L: ", blocks[l], file_sizes[blocks[l].file_id])
            for i in range(r, l, -1):
                if file_sizes[blocks[i].file_id] < file_sizes[blocks[l].file_id]:
                    # print(blocks[i], file_sizes[blocks[i].file_id])
                    
                    if blocks[i].data == ".":
                        continue
                    
                    for y in range(file_sizes[blocks[i].file_id]):
                        # print("Replacing", blocks[l], file_sizes[blocks[l+y].file_id], blocks[i], file_sizes[blocks[i].file_id])
                        file_sizes[blocks[l].file_id] -= 1
                        blocks[l+y], blocks[i-y] = blocks[i-y], blocks[l+y]
                    print_blocksystem(blocks, "a")
                    break
            else:
                print("no fitting blocks found")
                l += 1
            continue

        # print("Replacing", blocks[l], file_sizes[blocks[l].file_id], blocks[r], file_sizes[blocks[r].file_id])
        for i in range(file_sizes[blocks[r].file_id]):
            file_sizes[blocks[l].file_id] -= 1
            blocks[l+i], blocks[r-i] = blocks[r-i], blocks[l+i]
        # blocks[l], blocks[r] = blocks[r], blocks[l]
        print_blocksystem(blocks, "b")

    s = 0
    i = 0

    print_blocksystem(blocks)

    for i, b in enumerate(blocks):
        if b.file_id is None: continue
        s += i * b.file_id

    return s


if __name__ == "__main__":
    with open("example.txt") as f:
        data = f.read()
    blocks = parse_blocks()

    print(part1())
    print(part2())

