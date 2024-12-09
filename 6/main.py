from copy import deepcopy

def get_guard_location(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                return(x, y)

def main():
    map: list[list[str]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:

            map.append(list(line.removesuffix("\n")))

    saved_map: list[list[str]] = deepcopy(map)
    guard_location = get_guard_location(map)

    saved_guard_loc = guard_location

    movement: list[tuple[int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    uni_movement: int = 1

    current_movement: int = 0
    while True:
        print(uni_movement)
        new_x = guard_location[0] + movement[current_movement][0]
        new_y = guard_location[1] + movement[current_movement][1]
        print(new_x, new_y)
        print(guard_location)
        if (new_x < 0 or new_x >= len(map[0]) or
            new_y < 0 or new_y >= len(map)):
            uni_movement += 1
            break

        if map[new_y][new_x] == ".":
            map[new_y][new_x] = "^"
            map[guard_location[1]][guard_location[0]] = "X"
            guard_location = (new_x, new_y)
            uni_movement += 1
        elif map[new_y][new_x] == "X":
            map[new_y][new_x] = "^"
            map[guard_location[1]][guard_location[0]] = "X"
            guard_location = (new_x, new_y)
        else:
            current_movement = (current_movement + 1) % len(movement)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.txt"), "w+") as file:
        for line in map:
            file.write("".join(line) + "\n")

    cross_path: int = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if saved_map[y][x] == ".":
                stuck = True
                mod_map = deepcopy(saved_map)
                mod_map[y][x] = "0"

                movement: list[tuple[int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                current_movement: int = 0

                guard_location = saved_guard_loc

                for _ in range(len(map) * len(map[0])):
                    new_x = guard_location[0] + movement[current_movement][0]
                    new_y = guard_location[1] + movement[current_movement][1]
                    if (new_x < 0 or new_x >= len(map[0]) or
                        new_y < 0 or new_y >= len(map)):
                        stuck = False
                        break

                    if mod_map[new_y][new_x] == ".":
                        mod_map[new_y][new_x] = "^"
                        mod_map[guard_location[1]][guard_location[0]] = "X"
                        guard_location = (new_x, new_y)
                    elif mod_map[new_y][new_x] == "X":
                        mod_map[new_y][new_x] = "^"
                        mod_map[guard_location[1]][guard_location[0]] = "X"
                        guard_location = (new_x, new_y)
                    else:
                        current_movement = (current_movement + 1) % len(movement)

                if stuck:
                    cross_path += 1

    print(cross_path)

if __name__ == '__main__':
    main()
