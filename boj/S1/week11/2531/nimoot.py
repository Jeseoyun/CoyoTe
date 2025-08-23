n,d,k,c=map(int,input().split())

arr1 = []

for _ in range(n):
    arr1.append(int(input()))

arr = arr1+arr1[0:k]

fin = 0
for i in range(n+1):
    tmp = arr[i:i+k]
    tmp_s = set(tmp)
    ans = 0
    
    if len(tmp) == len(tmp_s):
        ans = k
    else:
        ans = len(tmp_s)

    if c not in tmp_s:
        ans += 1
        if ans == k+1:
            print(ans)
            exit()

    if fin < ans:
        fin = ans

print(fin)
