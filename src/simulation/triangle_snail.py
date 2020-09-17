# 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    elem_len = (n*(n+1))//2
    array = [[0]*i for i in range(1, n+1)]
    di = 0
    y = 0
    x = 0
    elem = 1
    directions = [(1, 0), (0, 1), (-1, -1)]
    for _ in range(elem_len):
        array[y][x] = elem
        direction = directions[di]
        new_y = y+direction[0]
        new_x = x+direction[1]
        if new_y < 0 or new_y >= n or new_x >= y+1 or array[new_y][new_x] != 0:
            di = (di+1)%3
            direction = directions[di]
            new_y = y+direction[0]
            new_x = x+direction[1]
        y = new_y
        x = new_x
        elem+=1
    return [col for row in array for col in row]

print(solution(4))
print(solution(5))
print(solution(6))