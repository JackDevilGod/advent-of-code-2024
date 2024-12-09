def main():
    left_list: list = []
    right_list: list = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        inp = file.readline()
        while inp != "":
            left, right = map(int, inp.split("   "))
            left_list.append(left)
            right_list.append(right)

            inp = file.readline()

    left_list.sort()
    right_list.sort()

    summation: float = 0

    while (len(left_list), len(right_list)) != (0, 0):
        summation += ((left_list.pop() - right_list.pop())**2)**0.5

    print(summation)


if __name__ == '__main__':
    main()
