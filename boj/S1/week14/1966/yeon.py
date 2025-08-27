# 프린터 큐
# https://www.acmicpc.net/problem/1966


import sys 
from collections import deque 

inputf = sys.stdin.readline 

def main():

    T = int(inputf())  # test cases 

    for tc in range(T):
        
        N, M = map(int, inputf().rstrip().split())
        importance = list(map(int, inputf().rstrip().split()))  # 문서의 중요도 리스트 

        q = deque([(i, importance[i]) for i in range(N)])  # (index, importance) 형식으로 deque 초기화

        count = 0  # 인쇄 된 무서의 수 
        
        while q:  # 큐가 빌 때까지 반복 
            current = q.popleft()  # 현재 문서 (가장 왼쪽)
            if any(current[1] < other[1] for other in q):  # 현재 문서보다 중요도가 높은 문서가 있는 경우 
                q.append(current)  # 현재 문서를 큐 맨 뒤로 삽입 
            else:
                count += 1  # 현재 문서 인쇄 
                if current[0] == M:  # 현재 문서 번호가 M(타겟 문서) 인 경우 
                    print(count)  # 인쇄 순서 출력 
                    break  # 타겟 문서가 인쇄되었으므로 반복 종료
    return

if __name__=='__main__':
    main()