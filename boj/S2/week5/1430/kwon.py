import sys
from collections import deque
input = sys.stdin.readline

def distance(x1, y1, x2, y2, r_squared):
    dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return dist_sq <= r_squared

def solve():

    N, R, D, X, Y = map(int, input().split())

    graph = [[0, 0]]
    for _ in range(N):
        graph.append(list(map(float, input().split())))

    v = [False] * (N + 1)
    
    q = deque([(X, Y, 0)])
    
    result = 0.0
    
    r_sq = R * R

    while q:
        cur_x, cur_y, count = q.popleft()

        for i in range(1, N + 1):
            target_x, target_y = graph[i]

            if not v[i] and distance(cur_x, cur_y, target_x, target_y, r_sq):
                v[i] = True

                result += (D / (2 ** count))
                
                q.append((target_x, target_y, count + 1))

    print(result)
solve()