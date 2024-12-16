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

    end_points: int = 0
    move_queue: list[tuple[tuple[int, int], str, int]] = [(starting_point, "E",  0)]
    explored: set[tuple[tuple[int, int], str, int]] = set()
    while True:
        current_position, direction, current_score = move_queue.pop(0)
        current_x, current_y = current_position
        explored.add((current_position, direction, current_score))

        if matrix[current_y + 1][current_x] == "." and direction != "S":
            if direction == "N":
                move_queue.append(((current_x, current_y + 1), "N", current_score + 1))
            else:
                move_queue.append(((current_x, current_y + 1), "N", current_score + 1001))
        elif matrix[current_y + 1][current_x] == "E" and direction != "S":
            if direction == "N":
                end_points = current_score + 1
            else:
                end_points = current_score + 1001
            break

        if matrix[current_y][current_x + 1] == "." and direction != "W":
            if direction == "E":
                move_queue.append(((current_x + 1, current_y), "E", current_score + 1))
            else:
                move_queue.append(((current_x + 1, current_y), "E", current_score + 1001))
        elif matrix[current_y][current_x + 1] == "E" and direction != "W":
            if direction == "E":
                end_points = current_score + 1
            else:
                end_points = current_score + 1001
            break

        if matrix[current_y - 1][current_x] == "." and direction != "N":
            if direction == "S":
                move_queue.append(((current_x, current_y - 1), "S", current_score + 1))
            else:
                move_queue.append(((current_x, current_y - 1), "S", current_score + 1001))
        elif matrix[current_y - 1][current_x] == "E" and direction != "N":
            if direction == "S":
                end_points = current_score + 1
            else:
                end_points = current_score + 1001
            break

        if matrix[current_y][current_x - 1] == "." and direction != "E":
            if direction == "W":
                move_queue.append(((current_x - 1, current_y), "W", current_score + 1))
            else:
                move_queue.append(((current_x - 1, current_y), "W", current_score + 1001))
        elif matrix[current_y][current_x - 1] == "E" and direction != "E":
            if direction == "W":
                end_points = current_score + 1
            else:
                end_points = current_score + 1001
            break

        move_queue = sorted(list(set(move_queue).difference(explored)),
                            key=lambda x: ((x[2] / distance_start_finish) +
                            abs(x[0][0] - end_point[0]) + abs(x[0][1] - end_point[1])))

    print(end_points)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
