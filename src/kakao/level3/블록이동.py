# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque, defaultdict
def nextpositions(pos, board):
    nexts=[]
    pos1, pos2 = pos
    y1, x1 = pos1
    y2, x2 = pos2
    
    # 상하좌우 추가
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
        next_y1, next_y2, next_x1, next_x2 = y1+dy[i], y2+dy[i], x1+dx[i], x2+dx[i]
        if board[next_y1][next_x1] == 0 and board[next_y2][next_x2] == 0:
            nexts.append({(next_y1, next_x1), (next_y2, next_x2)})
    
    # 현재 로봇이 가로로 놓여있다면
    if y1 == y2:
        for dy in [-1,1]:
            if board[y1+dy][x1] == 0 and board[y2+dy][x2] == 0:
                nexts.append({(y1, x1),(y2+dy, x1)})
                nexts.append({(y2,x2),(y1+dy, x2)})
    
    # 현재 로봇이 세로로 놓여있다면
    elif x1 == x2:
        for dx in [-1,1]:
            if board[y1][x1+dx] == 0 and board[y2][x2+dx] == 0:
                nexts.append({(y1, x1),(y1, x2+dx)})
                nexts.append({(y2, x2),(y2, x1+dx)})
    if board[y1-1][x1] == 0 and board[y2-1][x2]==0:
        nexts.append({(y1-1, x1), (y2-1, x2)})
    return nexts
def solution(board):
    n = len(board)

    # 벽 생성
    board.insert(0, [1]*n)
    board.append([1]*n)
    for row in board:
        row.insert(0, 1)
        row.append(1)
    
    visit = [] # set은 해시를 생성할 수 없어서 리스트로 구현
    start = {(1,1),(1,2)} # 시작 위치
    q = deque([(start,0)]) # 거리도 큐에 삽입
    visit.append(start) # 처음 위치 방문 처리
    while q:
        now, dist = q.popleft()
        if (n, n) in now: # 로봇이 n,n에 도착하면 거리 반환
            return dist
        for pos in nextpositions(now, board):
            # 다음 이동할 위치 중 방문하지 않은 곳만 q에 집어넣고 방문 처리
            if pos not in visit:
                q.append((pos,dist+1))
                visit.append(pos)
    return 0

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])