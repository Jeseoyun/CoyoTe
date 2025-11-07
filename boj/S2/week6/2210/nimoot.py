from collections import deque

arr = [list(input().split()) for _ in range(5)]

ans = set()

dxy = [[-1,0],[1,0],[0,1],[0,-1]]
for i in range(5):
    for j in range(5):
        queue = deque()
        queue.append((i, j, arr[i][j]))

        while queue:
            x, y, num = queue.popleft()

            if len(num) == 6:
                ans.add(num)
                continue

            for mov in dxy:
                nx, ny = x + mov[0], y + mov[1]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    queue.append((nx, ny, num + arr[nx][ny]))

print(len(ans))
