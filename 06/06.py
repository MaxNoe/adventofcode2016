from collections import Counter


def part_one():
    counters = [Counter() for _ in range(8)]

    with open('06/06.txt') as f:
        for line in f:
            for counter, letter in zip(counters, line):
                counter.update([letter])
        print(''.join(c.most_common(1)[0][0] for c in counters))


def part_two():
    counters = [Counter() for _ in range(8)]

    with open('06/06.txt') as f:
        for line in f:
            for counter, letter in zip(counters, line):
                counter.update([letter])
        print(''.join(c.most_common()[-1][0] for c in counters))


if __name__ == '__main__':
    part_one()
    part_two()
