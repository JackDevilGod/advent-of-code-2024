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

    end_points: int = 0
    move_queue: list[tuple[tuple[int, int], tuple[int, int], int]] = [(starting_point, (1, 0),  0)]
    explored: set[tuple[int, int]] = set()
    while True:
        current_position, direction, current_score = move_queue.pop(0)
        current_x, current_y = current_position
        explored.add(current_position)
        print(current_position)

        if current_position == end_point:
            end_points = current_score
            break

        up_offset: tuple[int, int] = (current_x, current_y - 1)
        if matrix[up_offset[1]][up_offset[0]] != "#" and up_offset not in explored:
            move_queue.append((up_offset, (0, -1),
                               current_score + abs(1001 * direction[0]) + abs(1 * direction[1])))

        down_offset: tuple[int, int] = (current_x, current_y + 1)
        if matrix[down_offset[1]][down_offset[0]] != "#" and down_offset not in explored:
            move_queue.append((down_offset, (0, 1),
                               current_score + abs(1001 * direction[0]) + abs(1 * direction[1])))

        right_offset: tuple[int, int] = (current_x + 1, current_y)
        if matrix[right_offset[1]][right_offset[0]] != "#" and right_offset not in explored:
            move_queue.append((right_offset, (1, 0),
                               current_score + abs(1001 * direction[1]) + abs(1 * direction[0])))

        left_offset: tuple[int, int] = (current_x - 1, current_y)
        if matrix[left_offset[1]][left_offset[0]] != "#" and left_offset not in explored:
            move_queue.append((left_offset, (-1, 0),
                               current_score + abs(1001 * direction[1]) + abs(1 * direction[0])))

        move_queue = sorted(list(set(move_queue).difference(explored)),
                            key=lambda x: ((x[2] / distance_start_finish) +
                            abs(x[0][0] - end_point[0]) + abs(x[0][1] - end_point[1])))

    print(end_points)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
