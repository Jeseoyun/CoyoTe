from collections import deque


INF = float('inf')


def make_graph(graph, a, b, w):
    if a not in graph:
        graph[a] = dict()
    if b not in graph[a]:
        graph[a][b] = 0

    if b not in graph:
        graph[b] = dict()
    if a not in graph[b]:
        graph[b][a] = 0

    graph[a][b] += w
    graph[b][a] += w


def bfs(graph, start, end):
    # graph[a][b] > 0인 경로만 이용해서 start->end 경로를 찾는다
    # parent 딕셔너리를 반환해서 경로를 추적할 수 있게 만든다

    parent = {start: None}
    queue = deque([start])

    while queue and end not in parent:
        cur = queue.popleft()

        for adj in graph[cur]:
            if adj in parent:
                continue
            if graph[cur][adj] <= 0:
                continue

            parent[adj] = cur
            queue.append(adj)

    if end not in parent:
        return None

    return parent


def max_flow(graph, start, end):
    total = 0

    while True:
        parent = bfs(graph, start, end)
        if not parent:
            break

        # 1. 최소 용량(병목 지점에서의 값) 구하기
        bottle_neck = INF
        node = end
        while parent[node]:
            p_node = parent[node]
            bottle_neck = min(bottle_neck, graph[p_node][node])
            node = p_node

        # 2. 병목만큼 보내기
        # 정방향 경로는 사용했으므로 삭제
        # 대신 역방향 경로에 유량을 더해줘서 다른 경로에서 추적 가능하게 만들어줌
        node = end
        while parent[node]:
            p_node = parent[node]
            graph[p_node][node] -= bottle_neck
            graph[node][p_node] += bottle_neck
            node = p_node

        # 3. 전체 유량에 더해주기
        total += bottle_neck

    return total


def main():
    N = int(input())
    graph = dict()

    for _ in range(N):
        a, b, w = input().split()
        w = int(w)

        make_graph(graph, a, b, w)

    print(max_flow(graph, 'A', 'Z'))


if __name__ == "__main__":
    main()