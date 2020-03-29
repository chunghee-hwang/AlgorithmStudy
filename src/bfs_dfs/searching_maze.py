# https://www.acmicpc.net/problem/2178
from sys import stdin
from collections import deque


def read_line():
    return stdin.readline()


def make_maze():
    maze_height, maze_width = map(int, read_line().split())
    v = [[False for _ in range(maze_width)] for _ in range(maze_height)]
    return maze_height, maze_width, v, [read_line() for _ in range(maze_height)]


def find_fastest_path(maze_height, maze_width, maze, v):
    q = deque()
    q.append((0, 0))  # (y, x)
    v[0][0] = True
    moved_count = 0
    while True:
        if v[maze_height - 1][maze_width - 1]:
            moved_count += 1
            return moved_count

        q_len = len(q)
        for _ in range(q_len):
            current_y, current_x = q.popleft()

            new_y = current_y - 1
            new_x = current_x
            if new_y >= 0 and maze[new_y][new_x] == '1' and not v[new_y][new_x]:
                v[new_y][new_x] = True
                q.append((new_y, new_x))

            new_y = current_y
            new_x = current_x - 1
            if new_x >= 0 and maze[new_y][new_x] == '1' and not v[new_y][new_x]:
                v[new_y][new_x] = True
                q.append((new_y, new_x))

            new_y = current_y + 1
            new_x = current_x
            if new_y < maze_height and maze[new_y][new_x] == '1' and not v[new_y][new_x]:
                v[new_y][new_x] = True
                q.append((new_y, new_x))

            new_y = current_y
            new_x = current_x + 1
            if new_x < maze_width and maze[new_y][new_x] == '1' and not v[new_y][new_x]:
                v[new_y][new_x] = True
                q.append((new_y, new_x))

        moved_count += 1


if __name__ == '__main__':
    n, m, visit, ma = make_maze()
    print(find_fastest_path(n, m, ma, visit))
