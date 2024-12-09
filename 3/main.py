import re


def main():
    pattern = r"(don't\(\))|(do\(\))|mul\(([0-9]+),([0-9]+)\)"
    txt: str = ""

    inp: str = input()

    while inp != "":
        txt += inp

        inp = input()

    matches = re.findall(pattern, txt)
    print(matches)

    sum: float = 0
    anabled = True
    for match in matches:
        fcommand, tcommand, x, y = match

        if fcommand == "don't()":
            anabled = False
        elif tcommand == "do()":
            anabled = True
            continue

        if anabled:
            sum += float(x) * float(y)

    print(sum)


if __name__ == '__main__':
    main()
