n, m = map(int, input().split())

arr = list(list(input()) for _ in range(n))

total = n*m # 전체에서

for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        # 연달아 만나면 -1
        elif arr[i][j] == '-':
            if j>0 and arr[i][j-1] == arr[i][j]:
                total -=1
        elif arr[i][j] == '|':
            if i>0 and arr[i-1][j] == arr[i][j]:
                total -=1

print(total)