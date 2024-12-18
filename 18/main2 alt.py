from time import perf_counter
from copy import deepcopy


def try_exc(matrix, size):
    queue: list[tuple[tuple[int, int], int]] = [((0, 0), 0)]
    while queue:
        position, steps = queue.pop(0)
        current_x, current_y = position
        matrix[current_y][current_x] = "O"

        if position == (size, size):
            return True

        if current_x + 1 <= size:
            if matrix[current_y][current_x + 1] == ".":
                queue.append(((current_x + 1, current_y), steps + 1))

        if current_x - 1 >= 0:
            if matrix[current_y][current_x - 1] == ".":
                queue.append(((current_x - 1, current_y), steps + 1))

        if current_y + 1 <= size:
            if matrix[current_y + 1][current_x] == ".":
                queue.append(((current_x, current_y + 1), steps + 1))

        if current_y - 1 >= 0:
            if matrix[current_y - 1][current_x] == ".":
                queue.append(((current_x, current_y - 1), steps + 1))

        queue = sorted(list(set(queue)),
                       key=lambda x: x[1] + abs(x[0][0] - size) + abs(x[0][1] - size))

    return False


def main():
    size = 70
    matrix: list[list[str]] = [["." for _ in range(size + 1)] for _ in range(size + 1)]

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        dat = file.readlines()
        for line in [line.removesuffix("\n") for line in dat]:
            print(line)
            data = line.split(",")
            matrix[int(data[1])][int(data[0])] = "#"

        for line in [line.removesuffix("\n") for line in reversed(dat)]:
            print(line)
            data = line.split(",")
            matrix[int(data[1])][int(data[0])] = "."
            working_matrix = deepcopy(matrix)

            if try_exc(working_matrix, size):
                break

        print(line)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
