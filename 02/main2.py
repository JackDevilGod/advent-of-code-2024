from copy import deepcopy
from time import perf_counter


def save_checker(inp: list[int]) -> bool:
    if len(set(inp)) != len(inp):
        return False

    if inp not in [sorted(inp), sorted(inp, reverse=True)]:
        return False

    for index in range(0, len(inp) - 1):
        if abs(inp[index] - inp[index + 1]) not in [1, 2 ,3]:
            return False

    return True


def main():
    sum_safe: int = 0

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:
            data: list[int] = [int(i) for i in line.split()]

            if save_checker(data):
                sum_safe += 1
            else:
                for index in range(0, len(data)):
                    mod_data = deepcopy(data)
                    mod_data.pop(index)
                    if save_checker(mod_data):
                        sum_safe += 1
                        break

    print(sum_safe)
    print(sum_safe == 531)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
