# https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html
from collections import defaultdict

graph = [['a', 'b', 29], ['a', 'f', 10], ['b', 'c', 16], ['b', 'g', 15], ['c', 'd', 12], ['d', 'g', 18],
         ['d', 'e', 22], ['e', 'g', 25], ['e', 'f', 27]]
n = 7
parent = defaultdict(lambda: '')
level = defaultdict(lambda: 1)


#  집합 초기화
def init_set():
    for v1, v2, weight in graph:
        parent[v1] = v1  # 자신의 루트는 자기 자신
        parent[v2] = v2  # 자신의 루트는 자기 자신


#  집합의 루트를 찾음
def find(u):
    if parent[u] == u:  # 루트 노드이면 return u
        return u
    #  그 외에는 자신의 루트를 찾으러 간다.
    parent[u] = find(parent[u])
    return parent[u]


#  u를 포함하고 있는 집합과 v를 포함하고 있는 집합을 합침
def union(u, v):
    # 서로의 루트 찾기
    u = find(u)
    v = find(v)
    if u == v:  # 루트가 같다면 이미 같은 트리
        return
    if level[u] > level[v]:  # u가 v보다 더 깊은 트리라면 swap
        u, v = v, u
    parent[u] = v  # u의 루트가 v가 되도록 함(깊은 트리 밑에 얕은 트리 넣기)
    if level[u] == level[v]:  # u와 v의 깊이가 같으면 v의 깊이를 늘려준다
        level[v] += 1


# 그래프의 간선을 가중치를 기준으로 정렬
def sort_graph_by_weight():
    graph.sort(key=lambda edge: edge[2])
    print(graph)


# 최소 신장 트리 만들기
def make_min_spanning_tree():
    mst = []
    init_set()
    for edge in graph:  # 가중치가 적은 순으로 정렬된 간선을 순회
        v1, v2, weight = edge
        if find(v1) != find(v2):  # 사이클이 안 생기면(v1과 v2가 같은 집합이 아니라면)
            union(v1, v2)  # 새로운 간선을 같은 집합으로 만들기
            mst.append(edge)  # 최소 신장 트리에 추가
        if len(mst) == n - 1:
            break
    return mst


def solution():
    sort_graph_by_weight()
    mst = make_min_spanning_tree()
    print(mst)


if __name__ == '__main__':
    solution()
