from collections import deque

N, L, R = map(int, input().split())

populations = [list(map(int, input().split())) for _ in range(N)]

dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))
def open(populations, start, visited):
    '''
    조건에 따라 국경선이 열리는 나라 찾기
    '''
    q = deque([start])
    visited[start[0]][start[1]] = True
    unite = [start]
    while q:
        y, x = q.popleft()

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not ((0 <= ny < N) and (0 <= nx < N)):
                continue
            if visited[ny][nx]:
                continue
            # 국경선을 열 조건이 아닌 경우
            if not (L <= abs(populations[y][x] - populations[ny][nx]) <= R):
                continue

            unite.append((ny, nx))
            q.append((ny, nx))
            visited[ny][nx] = True
    
    population_avg = 0
    for y, x in unite:
        population_avg += populations[y][x]
    population_avg //= len(unite)

    return unite, population_avg


def move(populations):
    # 연합을 해체하고, 모든 국경선을 닫는다.
    visited = [[False] * N for _ in range(N)]
    result = []

    # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                continue
            unite, unit_population = open(populations, (y, x), visited)

            # 연합의 수가 1일 경우(국경을 열지 않았을 경우)
            if len(unite) == 1:
                continue
            result.append((unite, unit_population))
    
    # 어떤 국경도 열리지 않았을 경우
    if not result:
        return False
        
    # 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
    # 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
    # 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
    for unite, unit_population in result:
        for y, x in unite:
            populations[y][x] = unit_population
    
    return True

day_cnt = 0
while True:
    if not move(populations):
        break
    # print(*populations, sep='\n')
    day_cnt += 1

print(day_cnt)