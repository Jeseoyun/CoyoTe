from collections import defaultdict, deque

INF = float('inf')

def floyd(n, dist_list):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_list[i][j] = min(dist_list[i][j], dist_list[i][k] + dist_list[k][j])

    # print(*dist_list, sep='\n')
    min_sum = INF
    result = 0
    for i, sum_dist in enumerate(map(sum, dist_list), start=1):
        if min_sum > sum_dist:
            min_sum = sum_dist
            result = i

    return result

def main():
    N, M = map(int, input().split())

    dist_list = [[INF] * N for _ in range(N)]
    for i in range(0, N):
        dist_list[i][i] = 0

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        dist_list[a][b] = 1
        dist_list[b][a] = 1
    
    print(floyd(N, dist_list))


if __name__ == "__main__":
    main()