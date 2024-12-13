from dataclasses import dataclass
import typing as t



@dataclass
class Node:
    y: int
    x: int
    value: int
    children: list["Node"]


def in_grid(y: int, x: int):
    if y < 0 or y > height - 1:
        return False
    
    if x < 0 or x > width - 1:
        return False
    
    return True


def walk(head):
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    for dy, dx in directions:
        if in_grid(head.y - dy, head.x - dx):
            if grid[head.y - dy][head.x - dx] == head.value + 1:
                head.children.append(walk(Node(head.y - dy, head.x - dx, grid[head.y - dy][head.x - dx], [])))
    
    return head


def score(trailhead: Node):
    reached = []

    def recurse(node: Node):
        if node.value == 9 and (node.y, node.x) not in reached:
            reached.append((node.y, node.x))
            return 1

        if not node.children:
            return 0

        for child in node.children:
            recurse(child)
        
        return 0

    recurse(trailhead)
    return len(reached)


def score2(node: Node):
    s = 0

    if node.value == 9:
        return 1
    
    if not node.children:
        return 0
    
    for child in node.children:
        s += score2(child)
    
    return s


def part1():
    return sum(score(graph) for graph in graphs)


def part2():
    return sum(score2(graph) for graph in graphs)


if __name__ == "__main__":
    with open("input.txt") as f:
        raw = f.read()
        grid = [[*map(lambda c: c if c == "." else int(c), line)] for line in raw.splitlines()]

    graphs = []
    height, width = len(grid), len(grid[0])

    for y in range(height):
        for x in range(width):
            if grid[y][x] == 0:
                graphs.append(walk(Node(y, x, grid[y][x], [])))

    print(part1())
    print(part2())
