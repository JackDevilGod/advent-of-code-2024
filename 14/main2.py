from time import perf_counter


def main():
    screen_width, screen_height = 101, 103
    robot_position: list[tuple[int, int]] = []
    robot_velocity: list[tuple[int, int]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            data: list[tuple] = [tuple([int(n) for n in _[2:].split(",")]) for _ in line.split()]
            robot_position.append(data[0])
            robot_velocity.append(data[1])

    print(robot_position)
    print(robot_velocity)
    n = 0
    running = True

    while running:
        n += 1
        matrix: list[list] = [[" " for _ in range(screen_width)] for _ in range(screen_height)]

        for index in range(len(robot_position)):
            robot_x, robot_y = robot_position[index]
            robot_velocity_x, robot_velocity_y = robot_velocity[index]

            robot_x += robot_velocity_x
            robot_y += robot_velocity_y

            if robot_x < 0:
                robot_x += screen_width
            elif robot_x >= screen_width:
                robot_x -= screen_width

            if robot_y < 0:
                robot_y += screen_height
            elif robot_y >= screen_height:
                robot_y -= screen_height

            robot_position[index] = (robot_x, robot_y)
            matrix[robot_y][robot_x] = "X"

        print(n)

        for row in matrix:
            if "XXXXXXXXXXXXXX" in "".join(row):
                running = False

    for row in matrix:
        print("".join(row))

    print(n)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
