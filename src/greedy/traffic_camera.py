# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30_001
    for route in routes:
        if not route[0] <= camera <= route[1]:
            camera = route[1]
            answer+=1
    return answer