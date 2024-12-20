from time import perf_counter
import re


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
            prize = (int(prize_x), int(prize_y))

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
        possible_moves: list[int] = []

        for amount_a in range(1, 101):
            for amount_b in range(1, 101):
                if (amount_a * button_a[0] + amount_b * button_b[0] == prize[0] and
                        amount_a * button_a[1] + amount_b * button_b[1] == prize[1]):
                    possible_moves.append(amount_a * 3 + amount_b)

        if possible_moves != []:
            total_tokens += min(possible_moves)

    print(total_tokens)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
