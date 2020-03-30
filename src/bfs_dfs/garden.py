# https://www.acmicpc.net/problem/18809
from sys import stdin
from collections import deque

color_green = 3
color_red = 4
len_row = 0
len_column = 0
garden = []
liquid_land_positions = deque()  # (y, x)
max_flower_count = 0


def read_line():
    return stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


def init_garden(n):
    global garden
    garden = [read_ints() for _ in range(n)]


def find_liquid_land_positions(n, m):
    for y in range(n):
        for x in range(m):
            if garden[y][x] == 2:
                liquid_land_positions.append((y, x))


def put_liquid(n, green, red, green_positions, red_positions, idx):
    global max_flower_count
    if green == 0 and red == 0:
        print('==')
        max_flower_count = max(simulate_garden(green_positions, red_positions), max_flower_count)
        return
    for idx2 in range(idx + 1, n):
        if green - 1 > -1:
            green -= 1
            green_positions.append(idx2)
            put_liquid(n, green, red, green_positions, red_positions, idx2)
            green_positions.pop()
            green += 1
        if red - 1 > -1:
            red -= 1
            red_positions.append(idx2)
            put_liquid(n, green, red, green_positions, red_positions, idx2)
            red_positions.pop()
            red += 1


def visit_land(time, q, y, x, liquid_color, visit, flower_positions):
    water = 0
    if garden[y][x] == water or (y, x) in flower_positions:
        return
    if liquid_color == color_red:
        other_color = color_green
    else:
        other_color = color_red
    visit_color_time = visit[y][x]
    visit_color, visit_time = visit_color_time
    if visit_time != -1:
        if visit_time == time and visit_color == other_color:
            flower_positions.append((y, x))
    else:
        visit_color_time[0] = liquid_color
        visit_color_time[1] = time
        q.append((y, x))


def spread_liquid(time, q, liquid_color, visit, flower_positions):
    y, x = q.popleft()
    if (y, x) in flower_positions:
        return

    new_y = y - 1
    new_x = x
    if new_y > -1:
        visit_land(time, q, new_y, new_x, liquid_color, visit, flower_positions)
    new_y = y
    new_x = x - 1
    if new_x > -1:
        visit_land(time, q, new_y, new_x, liquid_color, visit, flower_positions)
    new_y = y + 1
    new_x = x
    if new_y < len_row:
        visit_land(time, q, new_y, new_x, liquid_color, visit, flower_positions)
    new_y = y
    new_x = x + 1
    if new_x < len_column:
        visit_land(time, q, new_y, new_x, liquid_color, visit, flower_positions)


def simulate_garden(green_positions, red_positions):
    liquid_visit = [[[-1, -1] for _ in range(len_column)] for _ in range(len_row)]  # [color, time]
    green_q = deque()
    red_q = deque()
    time = 0
    flower_positions = []
    for green_position in green_positions:
        positions = liquid_land_positions[green_position]
        visit_color_time = liquid_visit[positions[0]][positions[1]]
        visit_color_time[0] = color_green
        visit_color_time[1] = time
        green_q.append(positions)
    for red_position in red_positions:
        positions = liquid_land_positions[red_position]
        visit_color_time = liquid_visit[positions[0]][positions[1]]
        visit_color_time[0] = color_red
        visit_color_time[1] = time
        red_q.append(positions)
    while green_q and red_q:
        # print('red_q: {}\ngreen_q: {}\n'.format(red_q, green_q))
        green_q_size = len(green_q)
        red_q_size = len(red_q)
        time += 1
        for _ in range(green_q_size):
            spread_liquid(time, green_q, color_green, liquid_visit, flower_positions)
        for _ in range(red_q_size):
            spread_liquid(time, red_q, color_red, liquid_visit, flower_positions)
    flower_created_cnt = len(flower_positions)
    print('flower_created_cnt:', flower_created_cnt)
    return flower_created_cnt


if __name__ == '__main__':
    len_row, len_column, len_green, len_red = read_ints()
    init_garden(len_row)
    find_liquid_land_positions(len_row, len_column)
    put_liquid(len(liquid_land_positions), len_green, len_red, deque(), deque(), -1)
    print('max_flower_count:', max_flower_count)
