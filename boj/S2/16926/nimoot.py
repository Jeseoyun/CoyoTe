# min(N, M) mod 2 = 0
# N, M 중 최솟값은 2의 배수

# N, M 중 최솟값을 K라고 하면, K//2번 회전 진행

n, m, r = map(int, input().split())
# print(n,m,r)

arr = list(list(map(int, input().split())) for _ in range(n))
# print(arr)

k = min(n, m) // 2

for _ in range(r):
    temp = [row[:] for row in arr]

    for q in range(k):
        # 가로
        for i in range(q, m-1-q):
            temp[q][i] = arr[q][i + 1]
            temp[n-1-q][i+1]=arr[n-1-q][i]
        # 세로
        for i in range(q, n-1-q):
            temp[i][m-1-q] = arr[i+1][m-1-q]
            temp[i+1][q]=arr[i][q]

    arr = temp
    
for i in range(n):
    print(*arr[i],end=' ')
    print()

# 이게 좀 더 깔꼼하네요^_^;
# for row in arr:
#     print(*row)
