def turn_dir(cur_dir):
    return (cur_dir + 1) % 4
def solution(n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_dir = 0
    y = 0; x = 0
    ans = [[0 for x in range(n)] for y in range(n)]
    number = 1
    while number <= n**2:
        ans[y][x] = number
        dy, dx = directions[cur_dir]
        if y + dy < 0 or y + dy > n - 1 or x + dx < 0 or x + dx > n - 1 or ans[y+dy][x+dx] > 0:
            cur_dir = turn_dir(cur_dir)
            dy, dx = directions[cur_dir]
        y += dy
        x += dx
        number += 1
    return ans