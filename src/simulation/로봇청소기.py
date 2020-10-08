# https://www.acmicpc.net/problem/14503
directions = [(-1,0),(0,1),(1,0),(0,-1)]

def solution(N, M, r, c, d, m):
    stop = False
    answer = 0
    while not stop:
        if m[r][c]!= 2:
            m[r][c] = 2
            answer += 1
        cnt = 0
        while cnt < 4:
            left = d-1
            if left < 0:
                left = 3
            lefty, leftx = directions[left]
            if m[r+lefty][c+leftx] == 0:
                d = left
                r+=lefty; c+=leftx
                break
            elif m[r+lefty][c+leftx] != 0:
                d = left
                cnt+=1
            if cnt == 4:
                if m[r-lefty][c-leftx] != 1:
                    r-=lefty; c-=leftx
                    cnt = 0
                else:
                    stop = True
                    break
    print(answer)  

def input():
    import sys
    N, M = map(int, sys.stdin.readline().split(' '))
    r,c,d = map(int, sys.stdin.readline().split(' '))
    m = [[*map(int, sys.stdin.readline().split(' '))] for _ in range(N)]
    return (N, M, r, c, d, m)
solution(*input())