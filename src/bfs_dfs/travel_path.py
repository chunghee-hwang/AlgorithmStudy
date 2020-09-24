# 여행 경로
# https://programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict,deque
import copy
def solution(tickets):
    nextpaths = defaultdict(list)
    cand = []
    n = len(tickets)
    for tidx, ticket in enumerate(tickets):
        a,b=ticket
        nextpaths[a].append((b, tidx))
    q = deque([["", "ICN",-1, 0, [], defaultdict(bool)]])
    while q:
        start,dest,tidx,usecount, path, visit = q.popleft()
        path.append(dest)
        visit[tidx]=True
        if usecount == n:
            cand.append(path)
            continue
        usecount+=1
        start = dest
        for dest,tidx in nextpaths[start]:
            if not visit[tidx]:
                q.append([start, dest, tidx, usecount, copy.copy(path), copy.copy(visit)])            
    return min(cand)

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]