def main():
    case_num = 1

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append((u, v))

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)
        tree_count = 0

        def dfs(cur, prev, nodes, edges):
            visited[cur] = True
            nodes.add(cur)
            for neighbor in graph[cur]:
                # 부모 방문 방지
                if neighbor == prev:
                    continue
                # 사이클 발견하면 빠져나오기
                if visited[neighbor]:
                    return False
                edges.add(tuple(sorted((cur, neighbor))))
                if not dfs(neighbor, cur, nodes, edges):
                    return False
            return True

        for i in range(1, n + 1):
            if not visited[i]:
                nodes = set()
                edges = set()

                # 사이클 확인
                if not dfs(i, 0, nodes, edges):
                    continue

                # 사이클이 없고, 간선의 수가 노드의 수 - 1이면 트리
                if len(edges) == len(nodes) - 1:
                    tree_count += 1

        if tree_count == 0:
            print(f"Case {case_num}: No trees.")
        elif tree_count == 1:
            print(f"Case {case_num}: There is one tree.")
        else:
            print(f"Case {case_num}: A forest of {tree_count} trees.")

        case_num += 1


if __name__ == "__main__":
    main()
