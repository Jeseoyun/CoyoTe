# 키 순서
# https://www.acmicpc.net/problem/2458

import sys 

inputf = sys.stdin.readline

def main():
    N, M = map(int, inputf().split())

    graph = [[False] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, inputf().split())
        graph[a][b] = True
    
    # 각 학생이 다른 학생들과 모두 연결이 되어 있는지 확인한다. : 플로이드워셜
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    # print(*graph, sep="\n")

    # 결과 확인
    cnt = 0
    for i in range(1, N+1):
        tmp = 0
        for j in range(1, N+1):
            if graph[i][j]:  # i 가 j 보다 작은 경우 
                tmp += 1
            if graph[j][i]:  # j 가 i 보다 작은 경우 
                tmp += 1
        # print(tmp)
        if tmp == N-1:  # 자기 자신을 제외한 모든 학생과 연결이 되어 있는 경우 (비교가 가능한 경우) 
            cnt += 1
    print(cnt)
    return 

if __name__=="__main__":
    main()