from math import cos, radians, sin


def process_boat_instruction(instruction, x_pos, y_pos, rotation):
    action = instruction[0]
    amount = int(instruction[1:])

    if(action == 'N' or (action == 'F' and rotation % 360 == 0)):
        y_pos += amount
    if(action == 'S' or (action == 'F' and rotation % 360 == 180)):
        y_pos -= amount
    if(action == 'E' or (action == 'F' and rotation % 360 == 90)):
        x_pos += amount
    if(action == 'W' or (action == 'F' and rotation % 360 == 270)):
        x_pos -= amount
    if(action == 'L'):
        rotation -= amount
    if(action == 'R'):
        rotation += amount

    return [x_pos, y_pos, rotation]


def rotate_point(point, angle):
    px, py = point

    rotated_x = cos(angle) * px - sin(angle) * py
    rotated_y = sin(angle) * px + cos(angle) * py

    return int(round(rotated_x)), int(round(rotated_y))


def process_waypoint_instruction(instruction, x_pos,
                                 y_pos, waypoint_x, waypoint_y):
    action = instruction[0]
    amount = int(instruction[1:])

    if(action == 'N'):
        waypoint_y += amount
    if(action == 'S'):
        waypoint_y -= amount
    if(action == 'E'):
        waypoint_x += amount
    if(action == 'W'):
        waypoint_x -= amount
    if(action in ['L', 'R']):
        if(action == 'R'):
            amount *= -1
        waypoint_x, waypoint_y = rotate_point(
                (waypoint_x, waypoint_y), radians(amount)
        )
    if(action == 'F'):
        x_pos += waypoint_x * amount
        y_pos += waypoint_y * amount

    return [x_pos, y_pos, waypoint_x, waypoint_y]


def get_manhattan_distance(x_pos, y_pos):
    return abs(x_pos) + abs(y_pos)


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

    x_pos = 0
    y_pos = 0
    rotation = 90

    # Part 1
    for instruction in lines:
        x_pos, y_pos, rotation = process_boat_instruction(
                instruction, x_pos, y_pos, rotation
        )

    print(f"Part 1: {str(get_manhattan_distance(x_pos, y_pos))}")

    x_pos = 0
    y_pos = 0
    waypoint_x = 10
    waypoint_y = 1

    # Part 2
    for instruction in lines:
        x_pos, y_pos, waypoint_x, waypoint_y = process_waypoint_instruction(
                instruction, x_pos, y_pos, waypoint_x, waypoint_y
        )

    print(f"Part 2: {str(get_manhattan_distance(x_pos, y_pos))}")
