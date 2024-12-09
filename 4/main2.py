pattern: list[str] = ["X", "M", "A", "S"]

def check_x(matrix:list[list[str]], x: int, y: int) -> int:
    if x - 1 >= 0 and x + 1 < len(matrix[0]):
        if y - 1 >= 0 and y + 1 < len(matrix):
            if matrix[y][x] == "A":
                got: list[str] = [matrix[y - 1][x - 1], matrix[y + 1][x - 1], matrix[y - 1][x + 1], matrix[y + 1][x + 1]]
                if got.count("M") == 2 and got.count("S") == 2 and (matrix[y - 1][x - 1] != matrix[y + 1][x + 1] or matrix[y + 1][x - 1] != matrix[y - 1][x + 1]):
                    return 1

    return 0

def main():
    matrix: list[list[str]] = []

    inp: str = input()
    while inp != "":
        matrix.append(list(inp))
        inp = input()

    summation: int = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            summation += check_x(matrix, x, y)

    print(summation)

if __name__ == '__main__':
    main()
