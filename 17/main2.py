from time import perf_counter
from math import trunc


def run(a, b, c, program):
    output: list = []
    start_index: int = 0
    operations = []
    while start_index + 1 < len(program):
        opcode: int = program[start_index]
        operand: int = program[start_index + 1]
        operations.append((opcode, operand))

        if opcode in [0, 2, 5, 6, 7]:
            if operand == 4:
                operand = a
            elif operand == 5:
                operand = b
            elif operand == 6:
                operand = c
            elif operand == 7:
                break

        match opcode:
            case 0:
                a = trunc(a/(2**operand))
            case 1:
                b = b ^ operand
            case 2:
                b = operand % 8
            case 3:
                if a != 0:
                    start_index = operand
                    continue
                else:
                    start_index += 2
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(operand % 8)
            case 6:
                b = trunc(a/(2**operand))
            case 7:
                c = trunc(a/(2**operand))

        start_index += 2

    return output


def main():
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        lines = file.readlines()
        program: list[int] = [int(_) for _ in lines[4].split(":")[1].split(",")]

    bits: list[int] = []

    for index, value in enumerate(program):
        bits.append(value * (8**(index+1)))

    a = bits.pop(0)

    for bit in bits:
        a ^= bit

    print(program)
    print(run(a, 0, 0, program))
    print(a)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
