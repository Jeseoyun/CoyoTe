# 바이러스 
# https://www.acmicpc.net/problem/2606

from collections import defaultdict, deque

def main():

    n_com = int(input())  
    n_pairs = int(input())

    network = defaultdict(list)

    # 네트워크 구성 
    for _ in range(n_pairs):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)


    dq = deque([1])
    visited = set()  # 방문 여부 set 
    while dq:
        curr = dq.popleft()
        visited.add(curr)  # 방문 처리 
        for i in range(len(network[curr])):  # 현재 컴퓨터와 연결된 컴퓨터 순회 
            if network[curr][i] in visited: continue   # 방문한 경우 스킵 
            dq.append(network[curr][i])  # deque 추가 
    
    print(len(list(visited))-1)  # 1번 컴퓨터 제외한 값 
        
    return

if __name__=='__main__':
    main()