from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
t = 0
cur_w = 0
i = 0

while i < n:
    t += 1
    cur_w -= bridge.popleft()
    if cur_w + trucks[i] <= L:
        bridge.append(trucks[i])
        cur_w += trucks[i]
        i += 1
    else:
        bridge.append(0)

t += w
print(t)