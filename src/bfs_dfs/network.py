# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

visit = None
graph = None
def dfs(vertex):
    if visit[vertex]:
        return
    visit[vertex] = True
    for v in graph[vertex]:
        dfs(v)
    
def solution(n, computers):
    global visit, graph
    answer = 0
    visit = [False] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    while True:
        try:
            vertex = visit.index(False)
            dfs(vertex)
            answer+=1
        except:
            break
    return answer