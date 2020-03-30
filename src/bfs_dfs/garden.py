# https://www.acmicpc.net/problem/18809
from sys import stdin
from collections import deque


def read_line():
    return stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


def init_garden(n):
    return [read_ints() for _ in range(n)]


def find_liquid_positions(n, m, g):
    positions = deque()
    for y in range(n):
        for x in range(m):
            if g[y][x] == 2:
                positions.append((y, x))
    return positions


def dump_green_red(positions, green, red, green_positions, red_positions, idx):
    if green >= 0 and red >= 0:
        print('position: {}, idx: {}'.format(positions, idx))
        print('green: {}, red: {}'.format(green, red))
        print('green_positions: {}, red_positions: {}\n'.format(green_positions, red_positions))


def put_liquid(positions, green, red, green_positions, red_positions, idx):

    if green == 0 and red == 0:
        dump_green_red(positions, green, red, green_positions, red_positions, idx)
        return
    for new_idx in range(idx + 1, len(positions)):
        if green - 1 > -1:
            green -= 1
            green_positions.append(positions[new_idx])
            put_liquid(positions, green, red, green_positions, red_positions, new_idx)
            green_positions.pop()
            green += 1

        if red - 1 > -1:
            red -= 1
            red_positions.append(positions[new_idx])
            put_liquid(positions, green, red, green_positions, red_positions, new_idx)
            red_positions.pop()
            red += 1


if __name__ == '__main__':
    len_row, len_column, len_green, len_red = read_ints()
    garden = init_garden(len_row)
    liquid_positions = find_liquid_positions(len_row, len_column, garden)
    put_liquid(liquid_positions, len_green, len_red, deque(), deque(), -1)
