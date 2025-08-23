# 효율적인 해킹 
# https://www.acmicpc.net/problem/1325

"""
신뢰하는 관계: 
    A가 B를 신뢰하는 경우 -> B를 해킹하면 A도 해킹할 수 있음 
    -> directed graph

# 서윤좌: 리스트를 사용해서 풀어라 -> 그래프를 리스트로 관리하라 ? 
"""
import sys
from collections import deque

inputf = sys.stdin.readline
printf = sys.stdout.write

def main():
    N, M = map(int, inputf().rstrip().split())
    graph = [[] for _ in range(N+1)]  # 컴퓨터 번호는 1부터 시작하므로 N+1
    for _ in range(M):
        a, b = map(int, inputf().split())
        graph[b].append(a)  # b를 해킹하면 a도 해킹할 수 있음

    # print(graph)

    # bfs
    def bfs(start):
        visited = [False] * (N + 1)
        queue = deque([start])
        visited[start] = True
        cnt = 0

        while queue:
            node = queue.popleft()
            cnt += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return cnt

    # 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 번호를 오름차순으로 출력
    counts = [0 for _ in range(N + 1)]
    # 모든 컴퓨터에 대해 bfs 수행
    for i in range(1, N + 1):
        cnt = bfs(i)
        counts[i] = cnt

    max_count = max(counts)
    # for i in range(1, N + 1):
    #     if counts[i] > max_count:
    #         max_count = counts[i]

    # print(counts)
    result = []
    for i in range(1, N + 1):
        if counts[i] == max_count:
            result.append(str(i))

    print(" ".join(result))
        
    return

if __name__=='__main__':
    main()