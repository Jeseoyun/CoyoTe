# 특정 거리의 도시 찾기

from collections import deque

INF = float('inf')

def bfs(graph, start):

    visited = [-1 for _ in range(len(graph.keys())+1)]
    visited[start] = 0

    dq = deque([start])
    while dq:
        v = dq.popleft()
        
        for adj_v in graph[v]:
            if visited[adj_v] == -1:
                visited[adj_v] = visited[v] + 1
                dq.append(adj_v)
        
    return visited


def main():

    N, M, K, X = map(int, input().split())

    graph = dict()
    for v in range(1, N+1):
        graph[v] = list()

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    dist = bfs(graph=graph, start=X)



    # 결과 출력 
    result = []
    for i in range(len(dist)):
        if dist[i] == K:
            result.append(i)
    
    if not result:
        print(-1)
    else:
        for i in sorted(result):
            print(i)


    return

if __name__=='__main__':
    main()