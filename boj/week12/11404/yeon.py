# 플로이드 
# https://www.acmicpc.net/problem/11404

INF = float('inf')

def main():

    n = int(input())  # 도시의 개수 
    m = int(input())  # 버스의 개수 

    # 인접 행렬 초기화 
    adj_matrix = [[INF] * n for _ in range(n)]

    # 인접 행렬에 자기 자신으로 가는 비용은 0으로 설정
    for i in range(n):
        adj_matrix[i][i] = 0

    # 버스 비용 입력 (a에서 b로 가는 비용 c)   
    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1  # 인덱스에 맞게 조정
        b -= 1  # 인덱스에 맞게 조정

        # 이미 존재하는 경로가 있다면 최소 비용으로 업데이트 -> 이런 조건이 있는 줄 몰랐음 ㅜ 
        if adj_matrix[a][b] > c:
            # a에서 b로 가는 비용이 더 작으면 업데이트
            adj_matrix[a][b] = c

    # 디버깅용: 초기 인접 행렬 출력
    # for i in range(n):
    #     print(*adj_matrix[i])

    # 플로이드-워셜 알고리즘
    for k in range(n):  # 중간 경유지 (k)
        for i in range(n):  # 출발 도시 (i)
            for j in range(n):  # 도착 도시 (j)
                if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:  # 더 저렴한 경로가 있다면
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]  # 경로 업데이트
    # 결과 출력
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == INF:  # 도달할 수 없는 경우
                adj_matrix[i][j] = 0  # 0으로 표시
        print(*adj_matrix[i])  # 행 단위로 출력
    return

if __name__=='__main__':
    main()