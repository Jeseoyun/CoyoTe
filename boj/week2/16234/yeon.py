# 인구 이동 

from collections import deque 

def main():
    N, L, R = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def check(r, c):
        """ 주변으로 연합국이 생길 가능성을 확인 

        Args:
            r (int): 좌표의 행 
            c (int): 좌표의 열 

        Returns:
            bool: 연합 가능 -> True , 연합 불가능 -> False 
        """
        for dr, dc in directions:
            nr, nc = r + dr, c + dc 
            if 0 <= nr < N and 0 <= nc < N:
                if L <= abs(grid[r][c] -  grid[nr][nc]) <= R:
                    return True 
        
        return False
    
    def bfs(r, c):
        """_summary_

        Args:
            r (int): 좌표의 행 
            c (int): 좌표의 열 
        """
        dq = deque([(r, c)])
        visited[r][c] = True  # 방문 여부 

        union = [(r, c)]  # 연합 좌표 리스트 
        sum_population = grid[r][c]  # 연합 총 인구 
        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 유효성 검사 1 (좌표 검사)
                    continue 
                if visited[nr][nc]:  # 유효성 검사 2 (방문 검사)
                    continue 
                if L <= abs(grid[r][c] - grid[nr][nc]) <= R:  # 유효성 검사 3 (인구 차이 검사)
                    union.append((nr, nc))  # 연합 추가 
                    visited[nr][nc] = True  # 방문 처리 
                    dq.append((nr, nc))  # 큐 추가 
                    sum_population += grid[nr][nc]  # 인구 누적 합

        if len(union) > 1:  # 연합 크기 1 이상 
            for i, j in union:  
                grid[i][j] = sum_population // len(union)  # 인구 분배 
            return True  # 정상적인 연합 생성 
        return False  # 비정상적인 종료 

    # bfs
    count = 0  # 일 수 카운트 
    while True:
        is_move = False  # 인구 이동 발생 플래그 
        visited = [[False for _ in range(N)] for _ in range(N)]  # 방문 여부 
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and check(i, j):  # 유효성 검사 1 & 2, 2번은 그냥 한 번 더 걸러준다 느낌 
                    if bfs(i, j):  # 정상적인 연합 생성 
                        is_move = True  # 이동 발생 
        
        if not is_move:  # 이동 없음 
            break 
        
        count += 1  

    print(count)

    return 

if __name__=='__main__':
    main()