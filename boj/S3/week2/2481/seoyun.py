# 1. 해밍거리이면 그래프로 연결한다
# 2. 그래프 탐색해서 최단 경로 찾는다


from collections import deque


def xor(c):
    return '1' if c == '0' else '0'


def find_candidates(code, K):
    candidates = []

    for i in range(K):
        cand = code[:i] + xor(code[i]) + code[i+1:]
        candidates.append(cand)

    return candidates


def bfs(graph, start, target, N):
    visited = [False] * (N + 1)
    queue = deque([(start, [start])])
    visited[start] = True

    while queue:
        cur, path = queue.popleft()

        if cur == target:
            return path

        for adj in graph[cur]:
            if visited[adj]:
                continue
            visited[adj] = True
            queue.append((adj, path + [adj]))

    return None


def main():
    N, K = map(int, input().split())
    codes = {i: input() for i in range(1, N+1)}
    rev_codes = {codes[i]: i for i in range(1, N+1)}

    M = int(input())
    queries = [int(input()) for _ in range(M)]

    graph = {node: [] for node in range(1, N+1)}

    for node in range(1, N+1):
        code = codes[node]
        # 미리 부호가 반전된 해밍거리 후보를 찾음
        candidates = find_candidates(code, K)

        for cand in candidates:
            # 일치하는게 있으면 그래프로 연결한다
            if cand in rev_codes:
                adj = rev_codes[cand]
                graph[node].append(adj)

    for target in queries:
        path = bfs(graph, 1, target, N)

        if path is None:
            print(-1)
        else:
            print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()