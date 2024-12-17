from time import perf_counter
from math import trunc


def main():
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        lines = file.readlines()
        a: int = int(lines[0].split(":")[1])
        b: int = int(lines[1].split(":")[1])
        c: int = int(lines[2].split(":")[1])
        program: list[int] = [int(_) for _ in lines[4].split(":")[1].split(",")]
    print(a, b, c)

    output: list = []
    start_index: int = 0
    while start_index + 1 < len(program):
        opcode: int = program[start_index]
        operand: int = program[start_index + 1]

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
            case 4:
                b = b ^ c
            case 5:
                output.append(operand % 8)
            case 6:
                b = trunc(a/(2**operand))
            case 7:
                c = trunc(a/(2**operand))

        start_index += 2

    print(a, b, c)
    print(program)
    print(",".join([str(_) for _ in output]))


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
