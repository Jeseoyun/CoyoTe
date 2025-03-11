# 바닥 장식 

from collections import deque 

def main():

    N, M  = map(int, input().split())
    floor = [input() for _ in range(N)]

    col_directions = [(1, 0), (-1, 0)]  # 열 방향 이동  
    row_directions = [(0, 1), (0, -1)]  # 행 방향 이동 
    visited = [[False for _ in range(M)] for _ in range(N)]  # 방문 여부 리스트 

    def bfs(r, c):
        dq = deque([(r, c)])
        visited[r][c] = True  # 방문 처리 

        while dq:
            r, c = dq.popleft()
            if floor[r][c] == "-": 
                # check for row directions 
                for dr, dc in row_directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M: continue  # 유효성 검사 1 (좌표 검사)
                    if floor[nr][nc] == "|": continue  # 유효성 검사 2 (타일 모양 검사)
                    if visited[nr][nc]: continue  # 유효성 검사 3 (방문 검사)

                    visited[nr][nc] = True  # 방문 처리 
                    dq.append((nr, nc))  # 큐 추가 

            else :  # floor[r][c] == "|"
                # check for col directions 
                for dr, dc in col_directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M: continue  # 유효성 검사 1 (좌표 검사
                    if floor[nr][nc] == "-": continue  # 유효성 검사 2 (타일 모양 검사)
                    if visited[nr][nc]: continue  # 유효성 검사 3 (방문 검사)

                    visited[nr][nc] = True  # 방문 처리 
                    dq.append((nr, nc))  # 큐 추가 
        return 
    
    count = 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c]:
                bfs(r, c)
                count += 1

    print(count)
            
    

    return

if __name__=='__main__':
    main()