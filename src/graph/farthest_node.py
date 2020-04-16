from collections import defaultdict, deque


def solution(n, edges):
    graph = defaultdict(lambda: [])
    visit = [False] * (n + 1)
    q = deque()
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    q.append(1)
    visit[1] = True
    distance = 0
    same_distance_vertexes = defaultdict(lambda :[])
    while q:
        distance += 1
        for _ in range(len(q)):
            v = q.popleft()
            next_vs = graph[v]
            for next_v in next_vs:
                if not visit[next_v]:
                    q.append(next_v)
                    same_distance_vertexes[distance].append(next_v)
                    visit[next_v] = True
    return len(same_distance_vertexes[max(same_distance_vertexes)])


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
