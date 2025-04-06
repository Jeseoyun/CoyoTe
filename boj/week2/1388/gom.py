'''
접근법

1. 가로 탐색

2. 세로 탐색 


카운트 집계

'''


N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(input()))


row_cnt, col_cnt=0, 0

# 1. 가로 탐색

row_flag=True
for i in range(N):
    row_flag=True
    for j in range(M):
        if row_flag==True and arr[i][j]=='-':
            row_flag=False
            row_cnt+=1
        if arr[i][j]=='|':
            row_flag=True


# 2. 세로 탐색

col_flag=True
for j in range(M):
    col_flag=True
    for i in range(N):
        if col_flag==True and arr[i][j]=='|':
            col_flag=False
            col_cnt+=1
        if arr[i][j]=='-':
            col_flag=True

print(row_cnt+col_cnt)
