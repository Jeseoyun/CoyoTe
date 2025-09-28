field = list(map(list, [input() for _ in range(12)]))

dyx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(sy, sx):
    visited = set()
    q = [(sy, sx)]
    visited.add((sy, sx))
    while q:
        y, x = q.pop(0)
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not(0 <= ny < 12 and 0 <= nx < 6):
                continue
            if (ny, nx) in visited:
                continue
            
            if field[ny][nx] == field[sy][sx]:
                visited.add((ny, nx))
                q.append((ny, nx))
    
    if len(visited) >= 4:
        for y, x in visited:
            field[y][x] = '.'
        return True
    return False

cnt = 0
while True:
    is_remove = False
    for i in range(12):
        for j in range(6):
            if field[i][j] == '.':
                continue

            if bfs(i, j):
                is_remove = True

    if not is_remove:
        break

    # 블록 내리기
    for j in range(6):
        stack = []
        for i in range(11, -1, -1):
            if field[i][j] == '.':
                continue
            
            stack.append(field[i][j])
            field[i][j] = '.'
        
        i = 11
        while stack:
            field[i][j] = stack.pop(0)
            i -= 1

    cnt += 1

print(cnt)