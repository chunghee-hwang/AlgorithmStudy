# https://www.acmicpc.net/problem/1717
from sys import stdin
def read_ints():
    return map(int, stdin.readline().split())

n, m = read_ints()
parent = [0] * (n+1)
level = [1] * (n+1)


def init(n):
    for u in range(n + 1):
        parent[u] = u


def find(u):
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    if level[u] > level[v]:
        u, v = v, u
    parent[u] = v
    if level[u] == level[v]:
        level[v] += 1




if __name__ == '__main__':
    output = []
    init(n)
    for _ in range(m):
        oper, a, b = read_ints()
        if oper == 0:
            union(a, b)
        else:  # oper == 1:
            output.append('YES') if find(a) == find(b) else output.append('NO')
    print('\n'.join(output))
