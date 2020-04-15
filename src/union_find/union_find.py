# https://www.crocus.co.kr/683
from collections import defaultdict

parent = defaultdict()
level = defaultdict()


def init(n):
    for i in range(1, n+1):
        parent[i] = i  # 자신의 루트는 자기 자신
        level[i] = 1  # 초기에 트리의 레벨은 1로 초기화


def find(u):
    #  루트 노드이면 return u
    if u == parent[u]:
        return u

    #  그 외에는 자신의 루트를 찾으러 간다.
    parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    u = find(u)
    v = find(v)

    #  루트가 같다면 이미 같은 트리
    if u == v:
        return

    #  u가 v보다 더 깊은 트리라면 swap
    if level[u] > level[v]:
        u, v = v, u

    # u의 루트가 v가 되도록(깊은 트리 밑에 얕은 트리 넣기)
    parent[u] = v

    # u와 v의 깊이가 같으면 v의 깊이를 늘려준다
    if level[u] == level[v]:
        level[v] += 1


if __name__ == '__main__':
    init(5)
    union(2, 1)
    union(4, 3)
    union(5, 3)
    union(5, 2)

    union(1, 4)
    same = find(5) == find(1)
    print(same)
