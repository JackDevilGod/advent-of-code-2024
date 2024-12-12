from time import perf_counter


def main():
    garden: list[list[str]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            garden.append(list(line))

    print(garden)
    flower_data: list[int] = []

    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if garden[y][x] in [".", "!"]:
                continue

            flower_area: int = 0
            flower_corners: int = 0

            type_flower: str = garden[y][x]
            queue: list[tuple[int, int]] = [(y, x)]
            while len(queue) > 0:
                flower_area += 1
                y1, x1 = queue.pop()

                if (y1 - 1, x1) not in queue and y1 - 1 >= 0:
                    if garden[y1 - 1][x1] == type_flower:
                        queue.append((y1 - 1, x1))

                if (y1 + 1, x1) not in queue and y1 + 1 < len(garden):
                    if garden[y1 + 1][x1] == type_flower:
                        queue.append((y1 + 1, x1))

                if (y1, x1 - 1) not in queue and x1 - 1 >= 0:
                    if garden[y1][x1 - 1] == type_flower:
                        queue.append((y1, x1 - 1))

                if (y1, x1 + 1) not in queue and x1 + 1 < len(garden[y1]):
                    if garden[y1][x1 + 1] == type_flower:
                        queue.append((y1, x1 + 1))

                if y1 - 1 >= 0:
                    if garden[y1 - 1][x1] not in [".", type_flower]:
                        if x1 - 1 >= 0:
                            if garden[y1][x1 - 1] not in [".", type_flower]:
                                flower_corners += 1
                        else:
                            flower_corners += 1

                        if x1 + 1 < len(garden[y1]):
                            if garden[y1][x1 + 1] not in [".", type_flower]:
                                flower_corners += 1
                        else:
                            flower_corners += 1

                    if garden[y1 - 1][x1] in [".", type_flower]:
                        if x1 - 1 >= 0:
                            if (garden[y1][x1 - 1] in [".", type_flower] and
                                    garden[y1 - 1][x1 - 1] not in [".", type_flower]):
                                flower_corners += 1

                        if x1 + 1 < len(garden[y1]):
                            if (garden[y1][x1 + 1] in [".", type_flower] and
                                    garden[y1 - 1][x1 + 1] not in [".", type_flower]):
                                flower_corners += 1

                if y1 + 1 < len(garden):
                    if garden[y1 + 1][x1] not in [".", type_flower]:
                        if x1 - 1 >= 0:
                            if garden[y1][x1 - 1] not in [".", type_flower]:
                                flower_corners += 1
                        else:
                            flower_corners += 1

                        if x1 + 1 < len(garden[y1]):
                            if garden[y1][x1 + 1] not in [".", type_flower]:
                                flower_corners += 1
                        else:
                            flower_corners += 1

                    if garden[y1 + 1][x1] in [".", type_flower]:
                        if x1 - 1 >= 0:
                            if (garden[y1][x1 - 1] in [".", type_flower] and
                                    garden[y1 + 1][x1 - 1] not in [".", type_flower]):
                                flower_corners += 1

                        if x1 + 1 < len(garden[y1]):
                            if (garden[y1][x1 + 1] in [".", type_flower] and
                                    garden[y1 + 1][x1 + 1] not in [".", type_flower]):
                                flower_corners += 1

                if y1 - 1 < 0 or y1 + 1 >= len(garden):
                    if x1 - 1 >= 0:
                        if garden[y1][x1 - 1] not in [".", type_flower]:
                            flower_corners += 1
                    else:
                        flower_corners += 1

                    if x1 + 1 < len(garden[y1]):
                        if garden[y1][x1 + 1] not in [".", type_flower]:
                            flower_corners += 1
                    else:
                        flower_corners += 1

                garden[y1][x1] = "."

            flower_data.append((flower_area * flower_corners))

            for y2 in range(len(garden)):
                for x2 in range(len(garden[y2])):
                    if garden[y2][x2] == ".":
                        garden[y2][x2] = "!"
    print(flower_data)

    print(sum(flower_data))


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
