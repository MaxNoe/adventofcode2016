import re
from collections import Counter
from functools import partial

room_re = re.compile(r'([a-z\-]+)([0-9]+)\[([a-z]+)\]')


def parse_room(line):
    m = room_re.match(line.strip())
    enc_name, sector_id, checksum = m.groups()
    sector_id = int(sector_id)
    return enc_name, sector_id, checksum


def is_valid(name, checksum):
    c = Counter(name.replace('-', ''))
    letters = [l[0] for l in sorted(c.most_common(), key=lambda x: (-x[1], x[0]))]
    return ''.join(letters[:5]) == checksum


def move_letter(letter, steps):
    if letter == '-':
        return ' '
    return chr((ord(letter) - ord('a') + steps) % 26 + ord('a'))


def decode_room_name(encrypted_name, sector_id):
    move_by_sector_id = partial(move_letter, steps=sector_id)
    return ''.join(map(move_by_sector_id, encrypted_name))


def solution():
    with open('04/04.txt') as f:
        id_sum = 0
        for line in f:
            enc_name, sid, checksum = parse_room(line)
            if is_valid(enc_name, checksum):
                id_sum += sid

                name = decode_room_name(enc_name, sid)
                if 'north' in name:
                    print('Part II: ', name, sid)

    print('Part I: ', id_sum)


if __name__ == '__main__':
    solution()
