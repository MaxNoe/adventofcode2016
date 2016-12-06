from hashlib import md5

door_id = 'reyedfim{}'


def md5hex(door_id, index):
    return md5(door_id.format(index).encode('ascii')).hexdigest()


def door1():
    password = ''
    index = 0
    while len(password) < 8:
        h = md5hex(door_id, index)
        if h.startswith('00000'):
            password += h[5]
        index += 1
    print('Door I:', password)


def door2():
    password = ['_'] * 8
    index = 0
    found = 0

    print('Door II:')
    print(''.join(password))
    while found < 8:
        h = md5hex(door_id, index)

        index += 1
        if h.startswith('00000'):
            try:
                pos = int(h[5])
            except ValueError:
                continue
            letter = h[6]
            if 0 <= pos < 8 and password[pos] == '_':
                found += 1
                password[pos] = letter
                print(''.join(password))


if __name__ == '__main__':
    door1()
    door2()
