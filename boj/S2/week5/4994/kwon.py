from collections import deque

def bfs(n):
    q = deque([1])
    while q:
        cur = q.popleft()
        for n_num in (cur * 10 + 0, cur * 10 + 1):
            if len(str(n_num)) > 100:
                continue
            
            if n_num % n == 0:
                return n_num
            q.append(n_num)

while True:
    n = int(input())
    if n == 0:
        break

    print(bfs(n))