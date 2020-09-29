# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061#qna
# 문제 작성: 본인

# 좌표에 있는 기둥과 보가 유효한 위치에 있는지 확인
def is_valid(x,y, wall, n):
    kidung_valid = False
    bo_valid = False
    
    # 좌표에 기둥이 있다면
    if wall[y][x][0]:
        # 좌표가 땅이거나, 바로 밑 좌표에 기둥이 있거나, 왼쪽 좌표에 보가 있거나 좌표에 보가 있으면 유효함
        kidung_valid =  y == 0 or (y-1>=0 and wall[y-1][x][0]) or (x-1>=0 and wall[y][x-1][1]) or wall[y][x][1]
    else:
        kidung_valid = True
    
    # 좌표에 보가 있다면
    if wall[y][x][1]:
        # 바로 밑 좌표에 기둥이 있거나, 바로 오른쪽 대각선 아래 좌표에 기둥이 있거나,
        # 바로 왼쪽과 오른쪽 좌표에 모두 보가 있을 경우 유효함
        bo_valid =  (y-1 >= 0 and wall[y-1][x][0]) or (y-1>=0 and x+1 < n and wall[y-1][x+1][0]) or \
    ((x-1 >=0 and wall[y][x-1][1]) and (x+1 < n and wall[y][x+1][1]))
    else:
        bo_valid = True
    return (kidung_valid and bo_valid) == True
    
def solution(n, build_frames):
    answer = []
    structures = {} # 기둥이나 보가 하나라도 있는 위치를 기록하는 사전
    N = n+1
    wall = [[[0,0] for x in range(N)] for y in range(N) ] # 벽면
    
    for build_frame in build_frames:
        x,y,a,b = build_frame
        
        # 구조물을 설치하거나 삭제하기 전 값을 저장
        previous_state = wall[y][x][a]
        
        # 벽면에 구조물을 설치하거나 제거해봄
        wall[y][x][a]=b
        
        # 구조물을 설치하거나 제거한 뒤 남은 구조물의 모든 좌표를 돌면서 모두 유효한지 검사
        valid = all([is_valid(structure[0], structure[1], wall, N) for structure in structures.keys()])
        if (x,y) not in structures:
            valid = is_valid(x,y, wall, N)
        
        # 설치하거나 제거한 결과가 유효하다면
        if valid:
            # 설치하거나 제거한 좌표에 기둥이나 보가 하나라도 남아있을 경우
            if wall[y][x][0] or wall[y][x][1]:
                # 구조물 좌표 저장
                structures[(x,y)] = True
            
            # 기둥과 보 모두 없을 경우
            else:
                # 구조물 좌표 삭제
                if (x,y) in structures:
                    del structures[(x,y)]
        # 설치하거나 제거한 결과가 유효하지 않다면
        else:
            # 이전에 있던 상태로 돌아감
            wall[y][x][a]=previous_state
        
    
    # 구조물 좌표들을 x, y를 기준으로 오름차순 정렬
    keys = sorted(list(structures.keys()))
    
    # 구조물 좌표들을 돌면서 벽면에 기둥이 있거나 보가 있을 경우 answer에 좌표 추가
    for key in keys:
        x,y=key
        # answer에 기둥 좌표 추가
        if wall[y][x][0]:
            answer.append([x,y,0])
        # answer에 보 좌표 추가
        if wall[y][x][1]:
            answer.append([x,y,1])
    return answer
# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))