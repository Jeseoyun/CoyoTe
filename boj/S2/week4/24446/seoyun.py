from collections import deque


def bfs(graph, start):
    visited = [-1 for _ in range(len(graph)+1)]

    queue = deque([(start, 0)])
    visited[start] = 0

    while queue:
        node, depth = queue.popleft()

        for adj in graph[node]:
            if visited[adj] != -1:
                continue

            queue.append((adj, depth+1))
            visited[adj] = depth + 1

    return visited


def main():
    N, M, R = map(int, input().split())  # 정점 수, 간선 수, 시작 정점

    graph = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    res = bfs(graph, R)

    for node in graph:
        print(res[node])


if __name__ == "__main__":
    main()