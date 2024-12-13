from time import perf_counter
import re
from sympy import symbols, Eq, solve
import sympy
import sympy.core
import sympy.core.numbers


def main():
    machines: dict[tuple[int, int], list[tuple[int, int]]] = {}
    pattern_button: str = r"Button [AB]: X\+([0-9]+), Y\+([0-9]+)"
    pattern_prize: str = r"Prize: X=([0-9]+), Y=([0-9]+)"

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        lines: list[str] = file.readlines()
        index: int = 0

        while index < len(lines):
            prize_x, prize_y = re.findall(pattern_prize, lines[index + 2])[0]
            prize = (int(prize_x) + 10000000000000, int(prize_y) + 10000000000000)

            button_x, button_y = re.findall(pattern_button, lines[index])[0]
            button_1 = (int(button_x), int(button_y))

            button_x, button_y = re.findall(pattern_button, lines[index + 1])[0]
            button_2 = (int(button_x), int(button_y))

            machines[prize] = ([button_1, button_2])

            index += 4

    print(machines)

    total_tokens: int = 0

    for prize in machines.keys():
        button_a = machines[prize][0]
        button_b = machines[prize][1]

        x, y = symbols('x,y')

        eq1 = Eq((x * button_a[0] + y * button_b[0]), prize[0])
        eq2 = Eq((x * button_a[1] + y * button_b[1]), prize[1])

        solution = solve((eq1, eq2), (x, y))
        print(type(solution))
        if (type(solution[x]) is sympy.core.numbers.Integer and
                type(solution[y]) is sympy.core.numbers.Integer):
            total_tokens += solution[x] * 3 + solution[y]

    print(total_tokens)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
