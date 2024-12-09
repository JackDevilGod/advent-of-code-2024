def main():
    matrix: list[list[str]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "x.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            data = list(line)
            matrix.append(data)

    x = 0
    ant = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "#":
                ant.add((x, y))
                x += 1

    print(x)
    print(ant)


if __name__ == '__main__':
    main()
