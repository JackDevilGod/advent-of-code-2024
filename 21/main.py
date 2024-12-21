from time import perf_counter


def find_path_to(pad: dict, key: str, start_key: tuple[int, int]) -> tuple[tuple[int, int],
                                                                           list[list[str]]]:
    queue: list[tuple[tuple[int, int], list[str]]] = [(start_key, [])]

    best_path_length: float = float("inf")
    best_paths: list[list[str]] = []
    while queue:
        position, path = queue.pop(0)

        if pad[position] == key:
            if best_path_length > len(path):
                best_path_length = len(path)
                best_paths = []
                best_paths.append(path)
            elif best_path_length == len(path):
                best_paths.append(path)
            else:
                break

        p_x, p_y = position

        if (p_x + 1, p_y) in pad.keys() and (p_x + 1, p_y) not in path:
            queue.append(((p_x + 1, p_y), path + [">"]))

        if (p_x - 1, p_y) in pad.keys() and (p_x - 1, p_y) not in path:
            queue.append(((p_x - 1, p_y), path + ["<"]))

        if (p_x, p_y + 1) in pad.keys() and (p_x, p_y + 1) not in path:
            queue.append(((p_x, p_y + 1), path + ["v"]))

        if (p_x, p_y - 1) in pad.keys() and (p_x, p_y - 1) not in path:
            queue.append(((p_x, p_y - 1), path + ["^"]))

        queue.sort(key=lambda x: len(x[1]))

    return ({v: k for k, v in pad.items()}[key], best_paths)


def combine(pre_paths, after_paths) -> list[list[str]]:
    if pre_paths == []:
        return [_ + ["A"] for _ in after_paths]
    else:
        temp_value = []
        for after_path in after_paths:
            for pre_path in pre_paths:
                temp_value.append(pre_path + after_path + ["A"])

        return temp_value


def prune(paths: list[list[str]]) -> list[list[str]]:
    shotest_length = float("inf")
    retun_list: list[list[str]] = []

    for path in paths:
        if len(path) < shotest_length:
            shotest_length = len(path)
            retun_list = []
            retun_list.append(path)
        elif len(path) == shotest_length:
            retun_list.append(path)

    return retun_list


def main():
    key_pad_decoder: dict[tuple[int, int], str] = {(0, 0): "7", (1, 0): "8", (2, 0): "9",
                                                   (0, 1): "4", (1, 1): "5", (2, 1): "6",
                                                   (0, 2): "1", (1, 2): "2", (2, 2): "3",
                                                   (1, 3): "0", (2, 3): "A"}
    directional_pad_decoder: dict[tuple[int, int], str] = {(1, 0): "^", (2, 0): "A",
                                                           (0, 1): "<", (1, 1): "v", (2, 1): ">"}

    codes: list[list[str]] = []
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            codes.append(list(line))

    end_codes: list[int] = []
    for code in codes:
        print(code)

        current_key_1 = (2, 3)
        after_1_paths: list[list[str]] = []
        for key in code:
            current_key_1, to_paths = find_path_to(key_pad_decoder, key, current_key_1)

            after_1_paths = combine(after_1_paths, to_paths)
        after_1_paths = prune(after_1_paths)

        after_2_paths: list[list[str]] = []
        for path in after_1_paths:
            current_key_2: tuple[int, int] = (2, 0)
            inter_after_2_paths: list[list[str]] = []
            for key in path:
                current_key_2, to_paths = find_path_to(directional_pad_decoder, key, current_key_2)
                inter_after_2_paths = combine(inter_after_2_paths, to_paths)

            after_2_paths += inter_after_2_paths
        after_2_paths = prune(after_2_paths)

        after_3_paths: list[list[str]] = []
        for path in after_2_paths:
            current_key_3: tuple[int, int] = (2, 0)
            inter_after_3_paths: list[list[str]] = []
            for key in path:
                current_key_3, to_paths = find_path_to(directional_pad_decoder, key, current_key_3)
                inter_after_3_paths = combine(inter_after_3_paths, to_paths)

            after_3_paths += inter_after_3_paths
        after_3_paths = prune(after_3_paths)

        end_codes.append(len(after_3_paths[0]))

    sum_com = 0
    for len_code, code in zip(end_codes, codes):
        sum_com += len_code * int("".join(code[:code.index("A")]))

    print(sum_com)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
