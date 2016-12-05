def load_instructions():
    with open('02.txt') as f:
        text = f.read()
    return map(str.strip, text.splitlines())


numpad = [[0, 0, 1, 0, 0],
          [0, 2, 3, 4, 0],
          [5, 6, 7, 8, 9],
          [0, 'A', 'B', 'C', 0],
          [0, 0, 'D', 0, 0]]


def find_number(pos, moves):
    pos = pos[:]
    for move in moves:
        if move == 'R':
            pos[1] = min(pos[1] + 1, 4 - abs(2 - pos[0]))
        elif move == 'L':
            pos[1] = max(pos[1] - 1, abs(2 - pos[0]))
        elif move == 'D':
            pos[0] = min(pos[0] + 1, 4 - abs(2 - pos[1]))
        elif move == 'U':
            pos[0] = max(pos[0] - 1, abs(2 - pos[1]))
    return pos


def find_code():
    code = []
    position = [2, 0]
    instructions = load_instructions()
    for moves in instructions:
        position = find_number(position, moves)
        code.append(numpad[position[0]][position[1]])
    return code


if __name__ == '__main__':
    print(find_code())
