MAX_W = 1000
N, M = map(int, input().split())

if N != 0:
    books = list(map(int, input().split()))
    cnt = 1
    remain_w = M
    for book in books:
        # 더 넣을 수 없으면 포장
        if remain_w < book:
            cnt += 1
            remain_w = M
        remain_w -= book

    print(cnt)
else:
    print(0)