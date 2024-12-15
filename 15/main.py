from time import perf_counter


def push_box(matrix: list[list], box_position: tuple[int, int], offset: tuple[int, int]) -> bool:
    match matrix[box_position[1] + offset[1]][box_position[0] + offset[0]]:
        case "#":
            return False
        case ".":
            matrix[box_position[1] + offset[1]][box_position[0] + offset[0]] = "O"
            matrix[box_position[1]][box_position[0]] = "."
            return True
        case "O":
            if push_box(matrix, (box_position[0] + offset[0], box_position[1] + offset[1]),
                        offset):
                matrix[box_position[1] + offset[1]][box_position[0] + offset[0]] = "O"
                matrix[box_position[1]][box_position[0]] = "."
                return True

    return False


def main():
    matrix: list[list[str]] = []
    movement: list[str] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        get_matrix: bool = True

        for line in [line.removesuffix("\n") for line in file]:
            if line == "":
                get_matrix = False

            if get_matrix:
                matrix.append(list(line))
            else:
                movement += list(line)

    fish_position: tuple[int, int] = (0, 0)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "@":
                fish_position = (x, y)
                break
        else:
            continue
        break

    movement_offset: tuple[int, int] = (0, 0)
    for move in movement:
        match move:
            case "^":
                movement_offset = (0, -1)
            case "v":
                movement_offset = (0, 1)
            case "<":
                movement_offset = (-1, 0)
            case ">":
                movement_offset = (1, 0)

        match matrix[fish_position[1] + movement_offset[1]][fish_position[0] + movement_offset[0]]:
            case "#":
                pass
            case ".":
                matrix[fish_position[1] +
                       movement_offset[1]][fish_position[0] + movement_offset[0]] = "@"
                matrix[fish_position[1]][fish_position[0]] = "."
                fish_position = (fish_position[0] + movement_offset[0],
                                 fish_position[1] + movement_offset[1])
            case "O":
                if push_box(matrix, (fish_position[0] + movement_offset[0],
                            fish_position[1] + movement_offset[1]),
                            movement_offset):
                    matrix[fish_position[1] +
                           movement_offset[1]][fish_position[0] + movement_offset[0]] = "@"
                    matrix[fish_position[1]][fish_position[0]] = "."
                    fish_position = (fish_position[0] + movement_offset[0],
                                     fish_position[1] + movement_offset[1])

    sum: int = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "O":
                sum += (100 * y) + x

    print(sum)
    print(sum == 1412971)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
