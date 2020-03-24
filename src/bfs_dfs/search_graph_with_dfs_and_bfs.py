# https://www.acmicpc.net/problem/1260
import sys
from collections import deque


def read_line():
    return sys.stdin.readline()


def read_ints():
    return list(map(int, read_line().split()))


def make_graph(vertex_length, edge_length):
    graph = [[] for _ in range(vertex_length + 1)]
    for idx in range(edge_length):
        v1, v2 = read_ints()
        graph[v1].append(v2)
        graph[v2].append(v1)
    for connected_vertex in graph:
        connected_vertex.sort()
    return graph


def visit_vertex(vertex, visited, output):
    output.append(str(vertex))
    visited[vertex] = True


def search_graph_with_dfs(graph, vertex, visited, output):
    if visited[vertex]:
        return

    visit_vertex(vertex, visited, output)
    connected_vertexes = graph[vertex]
    for connected_vertex in connected_vertexes:
        if not visited[connected_vertex]:
            search_graph_with_dfs(graph, connected_vertex, visited, output)


def search_graph_with_bfs(graph, start_vertex, vertex_length, output):
    visited = [False for _ in range(vertex_length + 1)]
    q = deque()
    visit_vertex(start_vertex, visited, output)
    q.append(start_vertex)
    while q:
        connected_vertexes = graph[q.popleft()]
        for connected_vertex in connected_vertexes:
            if not visited[connected_vertex]:
                visit_vertex(connected_vertex, visited, output)
                q.append(connected_vertex)


if __name__ == '__main__':
    n, m, v = read_ints()
    g = make_graph(n, m)
    visit = [False for _ in range(n + 1)]
    result_output = []
    search_graph_with_dfs(g, v, visit, result_output)
    print(' '.join(result_output))
    result_output.clear()
    search_graph_with_bfs(g, v, n, result_output)
    print(' '.join(result_output))
