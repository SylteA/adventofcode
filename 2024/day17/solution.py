
def combo(registers: dict[str, int], op: int):
    return {
        4: registers["A"],
        5: registers["B"],
        6: registers["C"],
    }.get(op, op)


def adv(pointer: int, registers: dict[str, int], operand: int, _buf: list[int]):
    registers["A"] >>= combo(registers, operand)
    return pointer + 2


def bxl(pointer: int, registers: dict[str, int], operand: int, _buf: list[int]):
    registers["B"] ^= operand
    return pointer + 2


def bst(pointer: int, registers: dict[str, int], operand: int, _buf: list[int]):
    registers["B"] = combo(registers, operand) % 8
    return pointer + 2


def jnz(pointer: int, registers: dict[str, int], operand: int, _buf: list[int]):
    if registers["A"] == 0:
        return pointer + 2

    return operand


def bxc(pointer: int, registers: dict[str, int], _operand: int, _buf: list[int]):
    registers["B"] ^= registers["C"]
    return pointer + 2


def out(pointer: int, registers: dict[str, int], operand: int, buf: list[int]):
    buf.append(combo(registers, operand) % 8)
    return pointer + 2


def bdv(pointer: int, registers: dict[str, int], operand: int, _: list[int]):
    registers['B'] = registers['A'] >> combo(registers, operand)
    return pointer + 2


def cdv(pointer: int, registers: dict[str, int], operand: int, _: list[int]):
    registers['C'] = registers['A'] >> combo(registers, operand)
    return pointer + 2


opcodes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


def part1(a: int, program: list[int]):
    pointer = 0

    buf = []
    registers = {"A": a, "B": 0, "C": 0}

    while pointer < len(program):
        opcode, operand = program[pointer:pointer+2]
        pointer = opcodes[opcode](pointer, registers, operand, buf)

    return buf


def part2(program: list[int]):
    a = 0
    for i in range(len(program))[::-1]:
        a *= 8
        while part1(a, program) != program[i:]:
            a += 1

    return a

def main():
    with open("input.txt") as f:
        raw = f.read()

    raw_registers, program = raw.split("\n\nProgram: ")

    registers = {
        key: int(val)
        for reg in raw_registers.replace("Register ", "").split("\n")
        for (key, val) in [reg.split(": ")]
    }
    program = [*map(int, program.split(","))]

    print(",".join(map(str, part1(registers["A"], program))))
    print(part2(program))


if __name__ == "__main__":
    main()
