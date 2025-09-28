from collections import deque


def bfs(graph, node):
    queue = deque([node])
    visited = set()

    while queue:
        curr = queue.popleft()

        for adj in graph[curr]:
            if adj in visited:
                continue
            queue.append(adj)
            visited.add(adj)

    return len(visited)


def main():
    N, M = map(int, input().split())

    graph = {node: [] for node in range(1, N+1)}
    rev_graph = {node: [] for node in range(1, N+1)}

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        rev_graph[b].append(a)

    is_fixed = 0

    for node in range(1, N+1):
        front = bfs(rev_graph, node)
        back = bfs(graph, node)

        if front + back == N - 1:
            is_fixed += 1

    print(is_fixed)


if __name__ == "__main__":
    main()
