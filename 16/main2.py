from time import perf_counter
from copy import deepcopy

matrix: list[list[str]] = []


def main():
    global matrix

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            matrix.append(list(line))

    running = True
    while running:
        copy_matrix = deepcopy(matrix)

        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == ".":
                    if [matrix[y + 1][x], matrix[y - 1][x],
                            matrix[y][x + 1], matrix[y][x - 1]].count("#") >= 3:
                        matrix[y][x] = "#"

        if matrix == copy_matrix:
            running = False

    start_point: tuple[int, int] = (0, 0)
    end_point: tuple[int, int] = (0, 0)

    for y in range(len(matrix)):
        for x in range(len(matrix)):
            if matrix[y][x] == "S":
                start_point = (x, y)
            elif matrix[y][x] == "E":
                end_point = (x, y)

    print(start_point)
    print(end_point)

    queue: list[tuple[int, tuple[int, int], tuple[int, int], set]] = [(0,
                                                                       start_point,
                                                                       (1, 0),
                                                                       set())]
    end_tiles: set = set()
    end_score: float | int = float("inf")
    visited: dict[tuple[tuple[int, int], tuple[int, int]], int] = dict()
    while len(queue) > 0:
        score, position, direction, path = queue.pop(0)
        print(position)
        if position == (11, 8):
            print()
        if (position, direction) in visited.keys():
            if visited[(position, direction)] < score:
                continue

        visited[(position, direction)] = score

        if position not in path:
            path.add(position)

        x, y = position
        dx, dy = direction

        if matrix[y - 1][x] == "." and (x, y - 1) not in path:
            queue.append((score + (1001 * abs(dx)) + (1 * abs(dy)),
                          (x, y - 1), (0, -1), path.copy()))
        elif matrix[y - 1][x] == "E" and (x, y - 1) not in path:
            if score < end_score:
                end_score = score
                end_tiles = path.union({(x, y - 1)})
            elif score == end_score:
                end_tiles.update(path.union({(x, y - 1)}))
            else:
                continue

        if matrix[y + 1][x] == "." and (x, y + 1) not in path:
            queue.append((score + (1001 * abs(dx)) + (1 * abs(dy)),
                          (x, y + 1), (0, 1), path.copy()))
        elif matrix[y + 1][x] == "E" and (x, y + 1) not in path:
            if score < end_score:
                end_score = score
                end_tiles = path.union({(x, y + 1)})
            elif score == end_score:
                end_tiles.update(path.union({(x, y + 1)}))
            else:
                continue

        if matrix[y][x + 1] == "." and (x + 1, y) not in path:
            queue.append((score + (1001 * abs(dy)) + (1 * abs(dx)),
                          (x + 1, y), (1, 0), path.copy()))
        elif matrix[y][x + 1] == "E" and (x + 1, y) not in path:
            if score < end_score:
                end_score = score
                end_tiles = path.union({(x + 1, y)})
            elif score == end_score:
                end_tiles.update(path.union({(x + 1, y)}))
            else:
                continue

        if matrix[y][x - 1] == "." and (x - 1, y) not in path:
            queue.append((score + (1001 * abs(dy)) + (1 * abs(dx)),
                          (x - 1, y), (-1, 0), path.copy()))
        elif matrix[y][x - 1] == "E" and (x - 1, y) not in path:
            if score < end_score:
                end_score = score
                end_tiles = path.union({(x - 1, y)})
            elif score == end_score:
                end_tiles.update(path.union({(x - 1, y)}))
            else:
                continue

    for x, y in [_[0] for _ in visited.keys()]:
        matrix[y][x] = "X"

    for row in matrix:
        print("".join(row))

    print(len(end_tiles))
    print(end_score)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
