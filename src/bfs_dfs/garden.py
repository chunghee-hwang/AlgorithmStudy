# https://www.acmicpc.net/problem/18809
from sys import stdin
from collections import deque

water = '0'
color_green = '3'
color_red = '4'
len_row = 0
len_column = 0
garden = []
liquid_land_positions = deque()  # (y, x)
len_liquid_land_positions = 0
flower_count = 0
max_flower_count = 0
time = 0

def read_ints():
    return list(map(int, read_line().split()))


def read_line():
    return stdin.readline()


def init_garden():
    global garden
    for y in range(len_row):
        line = read_line()
        for x in range(0, len_column*2, 2):
            if line[x] == '2':
                liquid_land_positions.append((y, x//2))
        garden.append(line)


def put_liquid(green, red, green_positions, red_positions, idx):
    global max_flower_count, flower_count
    if green == 0 and red == 0:
        simulate_garden(green_positions, red_positions)
        max_flower_count = max(flower_count, max_flower_count)
        flower_count = 0
        return
    for idx2 in range(idx + 1, len_liquid_land_positions):
        if green - 1 > -1:
            green -= 1
            green_positions.append(liquid_land_positions[idx2])
            put_liquid(green, red, green_positions, red_positions, idx2)
            green_positions.pop()
            green += 1
        if red - 1 > -1:
            red -= 1
            red_positions.append(liquid_land_positions[idx2])
            put_liquid(green, red, green_positions, red_positions, idx2)
            red_positions.pop()
            red += 1


def visit_land(q, y, x, liquid_color, visit, flower_exists):
    global flower_count

    if garden[y][x*2] == water or flower_exists[y][x]:
        return
    if liquid_color == color_red:
        other_color = color_green
    else:
        other_color = color_red
    visit_color_time = visit[y][x]
    visit_color, visit_time = visit_color_time
    if visit_time != -1:
        if visit_time == time and visit_color == other_color:
            flower_exists[y][x] = True
            flower_count += 1
    else:
        visit_color_time[0] = liquid_color
        visit_color_time[1] = time
        q.append((y, x))


def spread_liquid(q, liquid_color, visit, flower_exists):
    y, x = q.popleft()
    if flower_exists[y][x]:
        return
    if y-1 > -1:
        visit_land(q, y-1, x, liquid_color, visit, flower_exists)
    if x-1 > -1:
        visit_land(q, y, x-1, liquid_color, visit, flower_exists)
    if y+1 < len_row:
        visit_land(q, y+1, x, liquid_color, visit, flower_exists)
    if x+1 < len_column:
        visit_land(q, y, x+1, liquid_color, visit, flower_exists)


def simulate_garden(green_positions, red_positions):
    global time
    liquid_visit = [[[-1, -1] for _ in range(len_column)] for _ in range(len_row)]  # [color, time]
    green_q = deque()
    red_q = deque()
    flower_exists = [[False for _ in range(len_column)] for _ in range(len_row)]
    for green_position in green_positions:
        visit_color_time = liquid_visit[green_position[0]][green_position[1]]
        visit_color_time[0] = color_green
        visit_color_time[1] = time
        green_q.append(green_position)
    for red_position in red_positions:
        visit_color_time = liquid_visit[red_position[0]][red_position[1]]
        visit_color_time[0] = color_red
        visit_color_time[1] = time
        red_q.append(red_position)
    while green_q and red_q:
        green_q_size = len(green_q)
        red_q_size = len(red_q)
        time += 1
        for _ in range(green_q_size):
            spread_liquid(green_q, color_green, liquid_visit, flower_exists)
        for _ in range(red_q_size):
            spread_liquid(red_q, color_red, liquid_visit, flower_exists)


if __name__ == '__main__':
    len_row, len_column, len_green, len_red = read_ints()
    init_garden()
    len_liquid_land_positions = len(liquid_land_positions)
    put_liquid(len_green, len_red, deque(), deque(), -1)
    print(max_flower_count)
