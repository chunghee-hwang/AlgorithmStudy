from sys import stdin
from collections import deque
max_value_sum = 0


def read_line():
    return stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


def get_tri_sum(triangle, tri_size):
    global max_value_sum



if __name__ == '__main__':
    n = int(read_line())
    tri = [read_ints() for _ in range(n)]
    get_tri_sum(tri, n)
    print(max_value_sum)
