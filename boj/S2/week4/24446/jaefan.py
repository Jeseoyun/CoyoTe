# https://www.acmicpc.net/problem/24446
# 알고리즘 수업 - 너비 우선 탐색 3

import sys 
from collections import defaultdict, deque

inputf = sys.stdin.readline

def bfs(graph, start, N):
    # 각 노드까지의 거리를 저장하는 배열 (-1은 방문하지 않음을 의미)
    visited = [-1 for _ in range(N+1)]
    queue = deque([start])
    visited[start] = 0  # 시작 노드의 거리는 0
    
    while queue:
        node = queue.popleft()
        # 현재 노드와 연결된 모든 인접 노드 확인
        for neighbor in graph[node]:
            if visited[neighbor] == -1:  # 아직 방문하지 않은 노드라면
                visited[neighbor] = visited[node] + 1  # 거리 업데이트
                queue.append(neighbor)  # 큐에 추가
    return visited

def main():
    # N: 정점의 수, M: 간선의 수, R: 시작 정점
    N, M, R = map(int, inputf().split())
    
    # 인접 리스트로 그래프 표현 (무방향 그래프)
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, inputf().split())
        # 무방향 그래프이므로 양방향으로 연결
        graph[u].append(v)
        graph[v].append(u)
        
    # BFS로 각 노드까지의 거리 계산
    depth = bfs(graph, R, N)
    
    # 1번 노드부터 N번 노드까지의 거리 출력
    for i in range(1, N+1):
        print(depth[i]) 


if __name__ == "__main__":
    main()