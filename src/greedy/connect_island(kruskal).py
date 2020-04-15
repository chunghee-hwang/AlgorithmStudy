# https://programmers.co.kr/learn/courses/30/lessons/42861


#  집합 초기화
def init_set(costs):
    for v1, v2, weight in costs:
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


# 최소 신장 트리 만들기
def make_min_spanning_tree(costs, n):
    # mst = []
    mst_weight_sum = 0  # MST 가중치 누적 합
    mst_edge_count = 0  # MST 간선 개수
    init_set(costs)
    costs.sort(key=lambda edge: edge[2])  # 그래프의 간선을 가중치를 기준으로 정렬
    for edge in costs:  # 가중치가 적은 순으로 정렬된 간선을 순회
        v1, v2, weight = edge
        if find(v1) != find(v2):  # 사이클이 안 생기면(v1과 v2가 같은 집합이 아니라면)
            union(v1, v2)  # 새로운 간선을 같은 집합으로 만들기
            # mst.append(edge)  # 최소 신장 트리에 추가
            mst_weight_sum += weight
            mst_edge_count += 1
        if mst_edge_count == n - 1:  # 최소 신장 트리의 간선 개수가 n-1개가 되면 완료 처리
            break
    return mst_weight_sum


def solution(n, costs):
    global parent, level
    parent = [0] * n
    level = [1] * n
    answer = make_min_spanning_tree(costs, n)
    return answer


if __name__ == '__main__':
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
