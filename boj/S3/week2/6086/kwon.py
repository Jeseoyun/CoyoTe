# [최대 유량](https://www.acmicpc.net/problem/6086)
from collections import deque

def solve():
    n = int(input())
    
    # 알파벳 -> 인덱스 변환 (A-Z: 0-25, a-z: 26-51)
    def to_idx(c):
        if c.isupper():
            return ord(c) - ord('A')
        return ord(c) - ord('a') + 26
    
    # 용량 그래프 (양방향)
    capacity = [[0] * 52 for _ in range(52)]
    for _ in range(n):
        a, b, c = input().split()
        u, v, w = to_idx(a), to_idx(b), int(c)
        capacity[u][v] += w
        capacity[v][u] += w
    
    source, sink = to_idx('A'), to_idx('Z')
    total_flow = 0
    
    # BFS로 증가 경로 찾기
    while True:
        parent = [-1] * 52
        parent[source] = source
        q = deque([source])
        
        while q and parent[sink] == -1:
            curr = q.popleft()
            for next_node in range(52):
                if parent[next_node] == -1 and capacity[curr][next_node] > 0:
                    parent[next_node] = curr
                    q.append(next_node)
        
        if parent[sink] == -1:  # 더 이상 증가 경로 없음
            break
        
        # 경로상 최소 잔여 용량 계산
        flow = float('inf')
        node = sink
        while node != source:
            flow = min(flow, capacity[parent[node]][node])
            node = parent[node]
        
        # 유량 갱신
        node = sink
        while node != source:
            capacity[parent[node]][node] -= flow
            capacity[node][parent[node]] += flow
            node = parent[node]
        
        total_flow += flow
    
    print(total_flow)

if __name__ == "__main__":
    solve()