from collections import deque

def solve():
    n, k = map(int, input().split())
    
    # 이진수 문자열을 정수로 변환하여 딕셔너리에 저장 (값 -> 인덱스)
    val_to_idx = {}
    first_val = 0
    for i in range(n):
        val = int(input(), 2)
        val_to_idx[val] = i + 1
        if i == 0:
            first_val = val
    
    # BFS를 위한 초기화
    # parent[i]는 i번 노드로 오기 직전의 노드 번호를 저장 (경로 복원용)
    parent = [-1] * (n + 1)
    parent[1] = 0 # 시작 노드 방문 표시
    val_q = deque([first_val])
    
    # BFS: 1번 문자열에서 시작하여 모든 도달 가능한 문자열 탐색
    # 각 자릿수(K개)의 비트를 하나씩 뒤집어보며 존재하는지 확인 (해밍 거리 1 찾기)
    while val_q:
        curr_val = val_q.popleft()
        curr_idx = val_to_idx[curr_val]
        
        for i in range(k):
            next_val = curr_val ^ (1 << i) # i번째 비트 반전
            if next_val in val_to_idx:
                next_idx = val_to_idx[next_val]
                if parent[next_idx] == -1: # 미방문 노드인 경우
                    parent[next_idx] = curr_idx
                    val_q.append(next_val)

    m = int(input())
    for _ in range(m):
        x = int(input())
        if parent[x] == -1:
            print("-1")
        else:
            # parent 배열을 따라 역추적하여 경로 복원
            path = []
            curr = x
            while curr != 0:
                path.append(curr)
                curr = parent[curr]
            print(*(path[::-1])) # 경로를 올바른 순서로 출력

if __name__ == "__main__":
    solve()