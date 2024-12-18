from time import perf_counter
import os
from copy import deepcopy


def try_get(x, y, matrix) -> None | str:
    if y < 0 or x < 0:
        return None

    try:
        return matrix[y][x]
    except IndexError:
        return None


def main():
    size = 70
    matrix: list[list[str]] = [["." for _ in range(size + 1)] for _ in range(size + 1)]

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        byte_count: int = 0
        for line in [line.removesuffix("\n") for line in file]:
            byte_count += 1
            data = line.split(",")
            print(data)
            matrix[int(data[1])][int(data[0])] = "#"
            working_matrix = deepcopy(matrix)

            escapable = True
            while True:
                compare_matrix = deepcopy(working_matrix)

                for y in range(len(working_matrix)):
                    for x in range(len(working_matrix[y])):
                        adjacent = [try_get(x + 1, y, working_matrix),
                                    try_get(x - 1, y, working_matrix),
                                    try_get(x, y + 1, working_matrix),
                                    try_get(x, y - 1, working_matrix)]

                        if (x, y) == (0, 0) or (x, y) == (size, size):
                            if adjacent.count("#") == 2:
                                escapable = False
                                break
                        else:
                            if adjacent.count(None) == 1 and adjacent.count("#") >= 2:
                                working_matrix[y][x] = "#"
                            elif adjacent.count(None) == 2 and adjacent.count("#") >= 1:
                                working_matrix[y][x] = "#"
                            else:
                                if adjacent.count("#") >= 3:
                                    working_matrix[y][x] = "#"

                if compare_matrix == working_matrix:
                    break

            if not escapable:
                break

    print(byte_count)
    print(data)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
