from time import perf_counter

matrix: list[list[str]] = []


def main():
    global matrix

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            matrix.append(list(line))

    starting_point: tuple[int, int] = (0, 0)
    end_point: tuple[int, int] = (0, 0)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "S":
                starting_point = (x, y)
            elif matrix[y][x] == "E":
                end_point = (x, y)

    distance_start_finish: float = (((abs(starting_point[0] - end_point[0])) +
                                    (abs(starting_point[1] - end_point[1]))))

    move_queue: list[tuple[tuple[int, int], str, int, set]] = [(starting_point, "E",  0,
                                                                {starting_point})]
    tiles_best_paths: set = set()
    best_score: int | float = float("inf")
    while len(move_queue) > 0:
        current_position, direction, current_score, path = move_queue.pop(0)
        current_x, current_y = current_position
        print(current_position)

        if (matrix[current_y + 1][current_x] == "." and direction != "S" and
                (current_x, current_y + 1) not in path):
            if direction == "N":
                move_queue.append(((current_x, current_y + 1), "N",
                                   current_score + 1, path.union({(current_x, current_y + 1)})))
            else:
                move_queue.append(((current_x, current_y + 1), "N",
                                   current_score + 1001,
                                   path.union({(current_x, current_y + 1)})))
        elif matrix[current_y + 1][current_x] == "E" and direction != "S":
            if direction == "N" and current_score + 1 <= best_score:
                tiles_best_paths.update(path.union({(current_x, current_y + 1)}))
                best_score = current_score + 1
            elif current_score + 1001 <= best_score:
                best_score = current_score + 1001
                tiles_best_paths.update(path.union({(current_x, current_y + 1)}))

        if (matrix[current_y][current_x + 1] == "." and direction != "W" and
                (current_x + 1, current_y) not in path):
            if direction == "E":
                move_queue.append(((current_x + 1, current_y),
                                   "E",
                                   current_score + 1,
                                   path.union({(current_x + 1, current_y)})))
            else:
                move_queue.append(((current_x + 1, current_y),
                                   "E",
                                   current_score + 1001,
                                   path.union({(current_x + 1, current_y)})))
        elif matrix[current_y][current_x + 1] == "E" and direction != "W":
            if direction == "E" and current_score + 1 <= best_score:
                tiles_best_paths.update(path.union({(current_x + 1, current_y)}))
                best_score = current_score + 1
            elif current_score + 1001 <= best_score:
                best_score = current_score + 1001
                tiles_best_paths.update(path.union({(current_x + 1, current_y)}))

        if (matrix[current_y - 1][current_x] == "." and direction != "N" and
                (current_x, current_y - 1) not in path):
            if direction == "S":
                move_queue.append(((current_x, current_y - 1), "S", current_score + 1,
                                   path.union({(current_x, current_y - 1)})))
            else:
                move_queue.append(((current_x, current_y - 1), "S", current_score + 1001,
                                   path.union({(current_x, current_y - 1)})))
        elif matrix[current_y - 1][current_x] == "E" and direction != "N":
            if direction == "S" and current_score + 1 <= best_score:
                tiles_best_paths.update(path.union({(current_x, current_y - 1)}))
                best_score = current_score + 1
            elif current_score + 1001 <= best_score:
                best_score = current_score + 1001
                tiles_best_paths.update(path.union({(current_x, current_y - 1)}))

        if (matrix[current_y][current_x - 1] == "." and direction != "E" and
                (current_x - 1, current_y) not in path):
            if direction == "W":
                move_queue.append(((current_x - 1, current_y), "W", current_score + 1,
                                   path.union({(current_x - 1, current_y)})))
            else:
                move_queue.append(((current_x - 1, current_y), "W", current_score + 1001,
                                   path.union({(current_x - 1, current_y)})))
        elif matrix[current_y][current_x - 1] == "E" and direction != "E":
            if direction == "W" and current_score + 1 <= best_score:
                tiles_best_paths.update(path.union({(current_x - 1, current_y)}))
                best_score = current_score + 1
            elif current_score + 1001 <= best_score:
                best_score = current_score + 1001
                tiles_best_paths.update(path.union({(current_x - 1, current_y)}))

        move_queue = sorted(move_queue,
                            key=lambda x: ((x[2] / distance_start_finish) +
                                           abs(x[0][0] - end_point[0]) +
                                           abs(x[0][1] - end_point[1])))

    print(len(tiles_best_paths))


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
