def manhattan(x1: tuple[int, int], x2: tuple[int, int]) -> tuple[int, int]:
    return (x1[0] - x2[0]), (x1[1] - x2[1])


def main():
    matrix: list[list[str]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            data = list(line)
            matrix.append(data)

    antenna_locations: dict[str, list[tuple[int, int]]] = {}

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == ".":
                continue
            elif matrix[y][x] not in antenna_locations.keys():
                antenna_locations[matrix[y][x]] = [(x, y)]
            else:
                antenna_locations[matrix[y][x]].append((x, y))

    amount_antinode: int = 0
    anti_nodes: set = set()

    for freq in antenna_locations.keys():
        for i, location in enumerate(antenna_locations[freq]):
            saved_x = location
            for other_location in antenna_locations[freq][i + 1:]:
                location = saved_x
                print(location, other_location)
                distance = manhattan(location, other_location)
                print(distance)

                if location not in anti_nodes:
                    anti_nodes.add(location)
                    amount_antinode += 1

                if other_location not in anti_nodes:
                    anti_nodes.add(y)
                    amount_antinode += 1

                nodes_left: tuple[int, int] = (location[0] + distance[0], location[1] + distance[1])
                while (nodes_left[0] >= 0 and nodes_left[0] < len(matrix[0])
                        and nodes_left[1] >= 0 and nodes_left[1] < len(matrix)):
                    if (nodes_left[0] >= 0 and nodes_left[0] < len(matrix[0])
                            and nodes_left[1] >= 0 and nodes_left[1] < len(matrix)
                            and nodes_left not in anti_nodes):
                        amount_antinode += 1
                        anti_nodes.add(nodes_left)
                        print(nodes_left)
                    location = nodes_left
                    nodes_left = (location[0] + distance[0], location[1] + distance[1])

                nodes_right: tuple[int, int] = (other_location[0] - distance[0],
                                                other_location[1] - distance[1])
                while (nodes_right[0] >= 0 and nodes_right[0] < len(matrix[0])
                        and nodes_right[1] >= 0 and nodes_right[1] < len(matrix)):
                    if (nodes_right[0] >= 0 and nodes_right[0] < len(matrix[0])
                            and nodes_right[1] >= 0 and nodes_right[1] < len(matrix)
                            and nodes_right not in anti_nodes):
                        amount_antinode += 1
                        anti_nodes.add(nodes_right)
                        print(nodes_right)

                    other_location = nodes_right
                    nodes_right = (other_location[0] - distance[0], other_location[1] - distance[1])

    print(amount_antinode)


if __name__ == '__main__':
    main()
