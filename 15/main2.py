from time import perf_counter
from copy import deepcopy

matrix: list[list[str]] = []


def move_box(box_left_position: tuple[int, int],
             box_right_position: tuple[int, int],
             offset: tuple[int, int]):
    global matrix
    matrix[box_left_position[1]][box_left_position[0]] = "."
    matrix[box_right_position[1]][box_right_position[0]] = "."
    matrix[box_left_position[1] + offset[1]][box_left_position[0] + offset[0]] = "["
    matrix[box_right_position[1] + offset[1]][box_right_position[0] + offset[0]] = "]"


def push_box_ver(box_left_position: tuple[int, int],
                 box_right_position: tuple[int, int],
                 offset: tuple[int, int]) -> bool:
    global matrix
    copy_matrix = deepcopy(matrix)

    match (matrix[box_left_position[1] + offset[1]][box_left_position[0] + offset[0]],
           matrix[box_right_position[1] + offset[1]][box_right_position[0] + offset[0]]):
        case (".", "."):
            move_box(box_left_position, box_right_position, offset)
            return True
        case ("[", "]"):
            if push_box_ver((box_left_position[0] + offset[0], box_left_position[1] + offset[1]),
                            (box_right_position[0] + offset[0], box_right_position[1] + offset[1]),
                            offset):
                move_box(box_left_position, box_right_position, offset)
                return True
        case (".", "["):
            if push_box_ver((box_left_position[0] + offset[0] + 1,
                             box_left_position[1] + offset[1]),
                            (box_right_position[0] + offset[0] + 1,
                             box_right_position[1] + offset[1]),
                            offset):
                move_box(box_left_position, box_right_position, offset)
                return True
        case ("]", "."):
            if push_box_ver((box_left_position[0] + offset[0] - 1,
                             box_left_position[1] + offset[1]),
                            (box_right_position[0] + offset[0] - 1,
                             box_right_position[1] + offset[1]),
                            offset):
                move_box(box_left_position, box_right_position, offset)
                return True
        case ("]", "["):
            if (push_box_ver((box_left_position[0] + offset[0] + 1,
                              box_left_position[1] + offset[1]),
                             (box_right_position[0] + offset[0] + 1,
                              box_right_position[1] + offset[1]),
                             offset)
                and
                push_box_ver((box_left_position[0] + offset[0] - 1,
                              box_left_position[1] + offset[1]),
                             (box_right_position[0] + offset[0] - 1,
                              box_right_position[1] + offset[1]),
                             offset)):
                move_box(box_left_position, box_right_position, offset)
                return True

    matrix = copy_matrix
    return False


def push_box_hor(box_left_position: tuple[int, int],
                 box_right_position: tuple[int, int],
                 offset: tuple[int, int]) -> bool:
    global matrix
    copy_matrix = deepcopy(matrix)

    match (matrix[box_left_position[1] + offset[1]][box_left_position[0] + offset[0]],
           matrix[box_right_position[1] + offset[1]][box_right_position[0] + offset[0]]):
        case (".", "["):
            move_box(box_left_position, box_right_position, offset)
            return True
        case ("]", "."):
            move_box(box_left_position, box_right_position, offset)
            return True
        case ("]", "["):
            if offset[0] < 0:
                if push_box_hor((box_left_position[0] + (2* offset[0]),
                                 box_left_position[1] + offset[1]),
                                (box_left_position[0] + offset[0],
                                 box_left_position[1] + offset[1]),
                                offset):
                    move_box(box_left_position, box_right_position, offset)
                    return True
            else:
                if push_box_hor((box_right_position[0] + offset[0],
                                 box_right_position[1] + offset[1]),
                                (box_right_position[0] + (2 * offset[0]),
                                 box_right_position[1] + offset[1]),
                                offset):
                    move_box(box_left_position, box_right_position, offset)
                    return True

    matrix = copy_matrix
    return False


def main():
    global matrix
    movement: list[str] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        get_matrix: bool = True

        for line in [line.removesuffix("\n") for line in file]:
            if line == "":
                get_matrix = False

            if get_matrix:
                matrix.append(list(line.replace("#",
                                                "##").replace(".",
                                                              "..").replace("@",
                                                                            "@.").replace("O",
                                                                                          "[]")))
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

    for move in movement:
        movement_offset: tuple[int, int] = (0, 0)

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
                continue
            case ".":
                matrix[fish_position[1] +
                       movement_offset[1]][fish_position[0] + movement_offset[0]] = "@"
                matrix[fish_position[1]][fish_position[0]] = "."
                fish_position = (fish_position[0] + movement_offset[0],
                                 fish_position[1] + movement_offset[1])
                continue

        if move in ["^", "v"]:
            match matrix[fish_position[1] + movement_offset[1]][fish_position[0] +
                                                                movement_offset[0]]:
                case "[":
                    if push_box_ver((fish_position[0] + movement_offset[0],
                                     fish_position[1] + movement_offset[1]),
                                    (fish_position[0] + movement_offset[0] + 1,
                                     fish_position[1] + movement_offset[1]),
                                    movement_offset):
                        matrix[fish_position[1] + movement_offset[1]][fish_position[0] +
                                                                      movement_offset[0]] = "@"
                        matrix[fish_position[1]][fish_position[0]] = "."
                        fish_position = (fish_position[0] + movement_offset[0],
                                         fish_position[1] + movement_offset[1])
                        continue
                case "]":
                    if push_box_ver((fish_position[0] + movement_offset[0] - 1,
                                     fish_position[1] + movement_offset[1]),
                                    (fish_position[0] + movement_offset[0],
                                     fish_position[1] + movement_offset[1]),
                                    movement_offset):
                        matrix[fish_position[1] + movement_offset[1]][fish_position[0] +
                                                                      movement_offset[0]] = "@"
                        matrix[fish_position[1]][fish_position[0]] = "."
                        fish_position = (fish_position[0] + movement_offset[0],
                                         fish_position[1] + movement_offset[1])
                        continue
        else:
            match matrix[fish_position[1] + movement_offset[1]][fish_position[0] +
                                                                movement_offset[0]]:
                case "[":
                    if push_box_hor((fish_position[0] + movement_offset[0],
                                     fish_position[1] + movement_offset[1]),
                                    (fish_position[0] + (2 * movement_offset[0]),
                                     fish_position[1] + movement_offset[1]),
                                    movement_offset):
                        matrix[fish_position[1] + movement_offset[1]][fish_position[0] +
                                                                      movement_offset[0]] = "@"
                        matrix[fish_position[1]][fish_position[0]] = "."
                        fish_position = (fish_position[0] + movement_offset[0],
                                         fish_position[1] + movement_offset[1])
                        continue
                case "]":
                    if push_box_hor((fish_position[0] + (2 * movement_offset[0]),
                                     fish_position[1] + movement_offset[1]),
                                    (fish_position[0] + movement_offset[0],
                                     fish_position[1] + movement_offset[1]),
                                    movement_offset):
                        matrix[fish_position[1] + movement_offset[1]][fish_position[0] +
                                                                      movement_offset[0]] = "@"
                        matrix[fish_position[1]][fish_position[0]] = "."
                        fish_position = (fish_position[0] + movement_offset[0],
                                         fish_position[1] + movement_offset[1])
                        continue
    sum: int = 0
    for y in range(len(matrix)):
        print("".join(matrix[y]))
        for x in range(len(matrix[y])):
            if matrix[y][x] == "[":
                sum += (100 * y) + x

    print(sum)
    print(sum == 1429299)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
