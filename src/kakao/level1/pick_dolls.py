# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
from collections import deque

def init_y_idxs(w, h, b):
    result = [0 for _ in range(w)]
    for x in range(w):
        result[x] = 0
        for y in range(h-1, -1, -1):
            if b[y][x] == 0:
                result[x] = y+1
                break
    return result

def solution(board, moves):
    answer = 0
    stack = deque()
    width = len(board[0])
    height = len(board)    
    y_idxs = init_y_idxs(width, height, board)
    for move in moves:
        x = move-1
        y = y_idxs[x]
        if y >= height:
            continue
        doll = board[y][x]
        y_idxs[x]+=1
        if stack and stack[-1] == doll:
            stack.pop()
            answer+=2
        else:
            stack.append(doll)
    return answer