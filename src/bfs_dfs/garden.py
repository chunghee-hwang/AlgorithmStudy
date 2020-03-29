# https://www.acmicpc.net/problem/18809
from sys import stdin
from collections import deque

red_positions = deque()
green_positions = deque()
def read_line():
    return stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


def init_garden(n):
    return [read_ints() for _ in range(n)]


def find_liquid_positions(n, m, g):
    positions = []
    for y in range(n):
        for x in range(m):
            if g[y][x] == 2:
                positions.append((y, x))
    return positions


def put_liquid(positions, idx, red, green):
    if red == 0 and green == 0:
        if red_positions and green_positions:
            print('red_positions:', red_positions, 'green_positions:', green_positions)
        return

    len_positions = len(positions)
    if idx >= len_positions:
        return
    for idx in range(len_positions):
        if red > 0 and idx not in green_positions and idx not in red_positions:
            red_positions.append(idx)
            put_liquid(positions, idx + 1, red - 1, green)
            red_positions.pop()
        if green > 0 and idx not in red_positions and idx not in green_positions:
            green_positions.append(idx)
            put_liquid(positions, idx + 1, red, green - 1)
            green_positions.pop()


if __name__ == '__main__':
    len_row, len_column, len_green, len_red = read_ints()
    garden = init_garden(len_row)
    liquid_positions = find_liquid_positions(len_row, len_column, garden)
    print(garden)
    print(liquid_positions)

    put_liquid(liquid_positions, 0, len_red, len_green)
