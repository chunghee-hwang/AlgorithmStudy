# https://www.acmicpc.net/problem/1976
from sys import stdin


def read_line():
    return stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


n = int(read_line())
m = int(read_line())
parent = [0] * (n + 1)
level = [1] * (n + 1)


def init_tree():
    for u in range(n):
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


def check_trip_is_possible():
    trip_schedule = read_ints()
    prev_parent = find(trip_schedule[0])
    for idx in range(1, len(trip_schedule)):
        if prev_parent != find(trip_schedule[idx]):
            return False
    return True


if __name__ == '__main__':
    init_tree()
    for city in range(1, n + 1):
        connected = read_ints()
        for other_city in range(city + 1, n + 1):
            if connected[other_city - 1] == 1:
                union(city, other_city)
    print('YES') if check_trip_is_possible() else print('NO')
