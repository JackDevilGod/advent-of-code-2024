from time import perf_counter
import re


def solve_recursive(prize: tuple[int, int],
                    buttons: list[tuple[int, int]],
                    current_location: tuple[int, int],
                    tokens_used: int) -> tuple:
    if tokens_used >= 100 * len(buttons):
        return (float("inf"), float("inf"))

    return_value: list = []

    for move in buttons:
        current_x, current_y = current_location
        if current_x + move[0] == prize[0] and current_y + move[1] == prize[1]:
            return_value.append(tokens_used + 1)
        elif current_x + move[0] > prize[0] and current_y + move[1] > prize[1]:
            return_value.append(float("inf"))
        else:
            return_value.append(min(solve_recursive(prize,
                                                    buttons,
                                                    (current_x + move[0], current_y + move[1]),
                                                    tokens_used + 1)))

    return tuple(return_value)


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
        print(prize)
        total_tokens += min(solve_recursive(prize, machines[prize], (0, 0), 0))

    print(total_tokens)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
