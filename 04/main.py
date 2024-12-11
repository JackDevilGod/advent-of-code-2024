pattern: list[str] = ["X", "M", "A", "S"]


def check_hor(matrix: list[list[str]], x: int, y: int) -> int:
    amount: int = 0
    if x - 3 >= 0:
        if [matrix[y][x], matrix[y][x - 1], matrix[y][x - 2], matrix[y][x - 3]] == pattern:
            amount += 1

    if x + 3 < len(matrix[0]):
        if [matrix[y][x], matrix[y][x + 1], matrix[y][x + 2], matrix[y][x + 3]] == pattern:
            amount += 1

    return amount


def check_ver(matrix: list[list[str]], x: int, y: int) -> int:
    amount: int = 0
    if y - 3 >= 0:
        if [matrix[y][x], matrix[y - 1][x], matrix[y - 2][x], matrix[y - 3][x]] == pattern:
            amount += 1

    if y + 3 < len(matrix):
        if [matrix[y][x], matrix[y + 1][x], matrix[y + 2][x], matrix[y + 3][x]] == pattern:
            amount += 1

    return amount


def check_dia(matrix: list[list[str]], x: int, y: int) -> int:
    amount: int = 0

    if x - 3 >= 0:
        if y + 3 < len(matrix):
            if [matrix[y][x], matrix[y + 1][x - 1],
                    matrix[y + 2][x - 2], matrix[y + 3][x - 3]] == pattern:
                amount += 1

        if y - 3 >= 0:
            if [matrix[y][x], matrix[y - 1][x - 1],
                    matrix[y - 2][x - 2], matrix[y - 3][x - 3]] == pattern:
                amount += 1

    if x + 3 < len(matrix[0]):
        if y + 3 < len(matrix):
            if [matrix[y][x], matrix[y + 1][x + 1],
                    matrix[y + 2][x + 2], matrix[y + 3][x + 3]] == pattern:
                amount += 1

        if y - 3 >= 0:
            if [matrix[y][x], matrix[y - 1][x + 1],
                    matrix[y - 2][x + 2], matrix[y - 3][x + 3]] == pattern:
                amount += 1

    return amount


def main():
    matrix: list[list[str]] = []

    inp: str = input()
    while inp != "":
        matrix.append(list(inp))
        inp = input()

    summation: int = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            summation += check_hor(matrix, x, y)
            summation += check_ver(matrix, x, y)
            summation += check_dia(matrix, x, y)

    print(summation)


if __name__ == '__main__':
    main()
