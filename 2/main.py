from copy import deepcopy


def save_checker(inp: list[int]) -> bool:
    t = sorted(inp)
    f = sorted(inp, reverse=True)
    if inp in [sorted(inp), sorted(inp, reverse=True)]:
        for index in range(len(inp) - 1):
            dif = ((inp[index] - inp[index + 1])**2)**0.5
            if 1 > dif or dif  > 3:
                return False
        return True

    return False


def main():
    inp: str = input()

    sum_safe: int = 0

    while inp != "":
        data: list[int] = [int(i) for i in inp.split()]

        if save_checker(data):
            sum_safe += 1
        else:
            for i in range(len(data)):
                mod_list = deepcopy(data)
                mod_list.pop(i)
                if save_checker(mod_list):
                    sum_safe += 1
                    break

        inp = input()

    print(sum_safe)


if __name__ == '__main__':
    main()
