n, m = map(int, input().split())
if n != 0:
    arr = list(map(int, input().split()))
    count = 0
    while len(arr)>0:
        temp = arr[0]
        del arr[0]
        while len(arr)>0 and temp + arr[0] <=m:
            temp += arr[0]
            del arr[0]
        count += 1
    print(count)
else:
    print(0)