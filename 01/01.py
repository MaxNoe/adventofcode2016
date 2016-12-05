def get_input():
    with open('01.txt') as f:
        text = f.read()
    return text


def turn_left(direction):
    return -direction[1], direction[0]


def turn_right(direction):
    return direction[1], -direction[0]


def parse_instructions(text):
    instructions = [
        (turn_left if i[0] == 'L' else turn_right, int(i[1:]))
        for i in text.split(', ')
    ]
    return instructions


def go(position, direction, steps):
    px = position[0] + steps * direction[0]
    py = position[1] + steps * direction[1]
    return px, py


def find_bunny_hq_part1(instructions):

    position = 0, 0
    direction = 0, 1

    for turn, steps in instructions:
        direction = turn(direction)
        position = go(position, direction, steps)

    return position


def find_bunny_hq_part2(instructions):

    position = 0, 0
    direction = 0, 1
    positions = set()

    for turn, steps in instructions:
        direction = turn(direction)
        for _ in range(steps):
            position = go(position, direction, 1)
            if position in positions:
                return position
            positions.add(position)

    return position


if __name__ == '__main__':
    print('Part I')
    text = get_input()
    instructions = parse_instructions(text)
    hq_x, hq_y = find_bunny_hq_part1(instructions)
    print(abs(hq_x) + abs(hq_y))

    print('Part II')
    hq_x, hq_y = find_bunny_hq_part2(instructions)
    print(abs(hq_x) + abs(hq_y))
