import numpy as np


def load_triangles():
    return np.genfromtxt('03.txt')


def is_triangle_possible(a, b, c):
    return (a + b > c) & (a + c > b) & (b + c > a)


if __name__ == '__main__':
    triangles = load_triangles()
    print('Part I')
    mask = is_triangle_possible(*triangles.T)
    print(mask.sum())

    a, b, c = triangles.T
    triangles = np.concatenate([a[:], b[:], c[:]])
    triangles.shape = (-1, 3)
    mask = is_triangle_possible(*triangles.T)
    print(mask.sum())
