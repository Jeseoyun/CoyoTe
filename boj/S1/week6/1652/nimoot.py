n = int(input())

arr = list(list(input()) for _ in range(n))
# print(arr)

# 가로로 한 번 스캔 후
# 오른쪽 방향으로 90도 회전하여 쭉 스캔하려고 했는데...는 일단 빡구현

row = 0
col = 0

for i in range(n): # 행
    temp = 0
    for j in range(n): # 열
        if arr[i][j]=='.':
            temp += 1
        else:
            if temp >= 2:
                row+=1
            temp = 0
        if j == n-1 and temp >= 2:
            row +=1

for j in range(n): #열
    temp =0
    for i in range(n): #행
        if arr[i][j] =='.':
            temp += 1
        else:
            if temp >= 2:
                col += 1
            temp = 0
        if i == n-1 and temp >= 2:
            col += 1

print(row, col)
