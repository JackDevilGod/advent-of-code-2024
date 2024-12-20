from time import perf_counter


def dijkstra(matrix: list[list[str]]) -> dict:
    queue: list[tuple[int, int]] = []
    cost_memory: dict[tuple[int, int], float] = dict()

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            match matrix[y][x]:
                case "E":
                    queue.append((x, y))
                    cost_memory[(x, y)] = float("inf")
                    end_point = (x, y)
                case "S":
                    queue.append((x, y))
                    cost_memory[(x, y)] = 0
                case ".":
                    queue.append((x, y))
                    cost_memory[(x, y)] = float("inf")

    queue.sort(key=lambda x: cost_memory[x])

    while queue:
        p_x, p_y = queue.pop(0)
        cost = cost_memory[(p_x, p_y)]

        if cost == float("inf"):
            break

        if (p_x, p_y) == end_point:
            cost_memory[end_point] = cost
            return cost_memory

        for offset in range(-1, 2, 2):
            if (p_x + offset, p_y) in queue:
                if cost_memory[(p_x + offset, p_y)] > cost + 1:
                    cost_memory[(p_x + offset, p_y)] = cost + 1

            if (p_x, p_y + offset) in queue:
                if cost_memory[(p_x, p_y + offset)] > cost + 1:
                    cost_memory[(p_x, p_y + offset)] = cost + 1

        queue.sort(key=lambda x: cost_memory[x])

    return cost_memory


def main():
    matrix: list[list[str]] = []
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            matrix.append(list(line))

    for row in matrix:
        print("".join(row))

    time_memory = dijkstra(matrix)

    amount: int = 0

    for begin_short in time_memory.keys():
        for end_short in time_memory.keys():
            if (begin_short == end_short or
                    abs(begin_short[0] - end_short[0]) + abs(begin_short[1] - end_short[1]) > 20):
                continue

            if time_memory[end_short] - (time_memory[begin_short] +
                                         abs(begin_short[0] - end_short[0]) +
                                         abs(begin_short[1] - end_short[1])) >= 100:
                amount += 1

    print(f"the amount shortcuts fast then x:{amount}")
    print(amount == 1020507)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
