# 도시와 비트코인 

from collections import deque 


def main():
    N, M = map(int, input().split())
    city = list()
    directions = [[1, 0], [0, 1]]
    for _ in range(M):
        city.append(list(map(int, input().split())))


    if N == M == 1:
        print('Yes')
        return
    
    
    def is_valid(r, c, visited):
        if not (0 <= r < M and 0 <= c < N and (r, c) not in visited and city[r][c]==1):
            return False 
        return True 
    
    def bfs(start):
        visited = set()
        dq = deque([start])
        while dq:
            curr_r, curr_c = dq.popleft()
            for dr, dc in directions:
                next_r, next_c = curr_r + dr, curr_c + dc 
                if is_valid(next_r, next_c, visited):                
                    if next_r == M-1 and next_c == N-1:
                        return True 
                    dq.append((next_r, next_c))
                    visited.add((next_r, next_c))
        if (M-1, N-1) not in visited:
            return False
        return True 

    if bfs((0,0)):
        print('Yes')
    else:
        print('No')

    return

if __name__=='__main__':
    main()