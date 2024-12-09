def main():
    inp = input()
    left_list: list = []
    right_list: list = []

    while inp != "":
        left, right = map(int, inp.split("   "))
        left_list.append(left)
        right_list.append(right)

        inp = input()

    left_list.sort()
    right_list.sort()

    summation: float = 0

    for num in left_list:
        summation += num * right_list.count(num)

    print(summation)


if __name__ == '__main__':
    main()