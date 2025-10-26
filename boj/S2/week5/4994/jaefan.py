# 배수 찾기 
# https://www.acmicpc.net/problem/4994

import sys 
from collections import deque

inputf = sys.stdin.readline

def find_multiple_bfs(N):
    """
    N의 배수 중에서 1과 0으로만 이루어진 가장 작은 수를 찾는다.
    BFS + 모듈러 연산을 사용하여 효율적으로 탐색
    """
    # N이 1이면 답은 1
    if N == 1:
        return "1"
    
    # BFS 초기화
    queue = deque()
    visited = [False] * N
    
    # 시작점: 숫자 '1'부터 시작
    start_remainder = 1 % N
    queue.append((start_remainder, "1"))
    visited[start_remainder] = True
    
    while queue:
        remainder, num_str = queue.popleft()
        
        # 나머지가 0이면 N의 배수를 찾은 것
        if remainder == 0:
            return num_str
        
        # 현재 숫자 뒤에 '0'을 추가하는 경우
        new_remainder = (remainder * 10) % N
        if not visited[new_remainder]:
            visited[new_remainder] = True
            queue.append((new_remainder, num_str + "0"))
        
        # 현재 숫자 뒤에 '1'을 추가하는 경우
        new_remainder = (remainder * 10 + 1) % N
        if not visited[new_remainder]:
            visited[new_remainder] = True
            queue.append((new_remainder, num_str + "1"))
    
    return None

def find_multiple(N):
    
    M = 1 
    queue = deque()
    queue.append(M)
    while queue:
        M = queue.popleft()

        # M 뒤에 0을 추가하는 경우 
        if int(str(M)+'0') % N == 0:
            return int(str(M)+'0')
        # M 뒤에 1을 추가하는 경우 
        if int(str(M)+'1') % N == 0:
            return int(str(M)+'1')
        queue.append(int(str(M)+'0'))
        queue.append(int(str(M)+'1'))
    return None 


def main():
    while True:
        N = int(inputf())
        if N == 0:
            break
        # BFS 기반 솔루션
        result = find_multiple(N)
        print(result)
        
        # # 브루트 포오스 (레거시)
        # max = int('9'*99) + 1
        # for i in range(1, max):
        #     if i % N == 0 and all(digit in ['0', '1'] for digit in str(i)):
        #         print(i)
        #         break



    return 

if __name__ == "__main__":
    main()