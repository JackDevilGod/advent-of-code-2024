from time import perf_counter
from pprint import pprint


def main():
    matrix: list[list[int]] = []
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            matrix.append([int(_) for _ in list(line)])

    pprint(matrix)

    start_queue: list = []

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                start_queue.append((y, x, 0))

    print(start_queue)
    amount_start = len(start_queue)

    trail_paths: int = 0
    for start_point in start_queue:
        print(f"{start_queue.index(start_point)}/{amount_start}")
        queue: list = []
        queue.append(start_point)
        while len(queue) > 0:
            y, x, height = queue.pop(0)

            if height == 9:
                trail_paths += 1
                continue

            if y - 1 >= 0:
                if matrix[y - 1][x] - height == 1:
                    queue.append((y - 1, x, matrix[y - 1][x]))

            if y + 1 < len(matrix):
                if matrix[y + 1][x] - height == 1:
                    queue.append((y + 1, x, matrix[y + 1][x]))

            if x - 1 >= 0:
                if matrix[y][x - 1] - height == 1:
                    queue.append((y, x - 1, matrix[y][x - 1]))

            if x + 1 < len(matrix[y]):
                if matrix[y][x + 1] - height == 1:
                    queue.append((y, x + 1, matrix[y][x + 1]))

    print(trail_paths)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
