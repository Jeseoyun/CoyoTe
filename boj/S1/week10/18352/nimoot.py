from collections import deque  # BFS에 사용할 큐 자료구조 deque를 임포트

# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시 번호 x 입력 받기
n, m, k, x = map(int, input().split())

# 그래프 초기화: 각 도시마다 연결된 도시 리스트를 저장할 리스트 생성
graph = [[] for _ in range(n + 1)]

# 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())  # a → b로 가는 단방향 도로
    graph[a].append(b)

# 각 도시까지의 최단 거리 정보를 저장하는 리스트 초기화
# -1은 아직 방문하지 않은 도시를 의미함
distance = [-1] * (n + 1)

# 출발 도시의 거리는 0으로 설정
distance[x] = 0

# BFS를 위한 큐 초기화, 출발 도시 x를 먼저 넣음
queue = deque([x])

# BFS 수행
while queue:
    now = queue.popleft()  # 현재 도시 꺼내기
    # 현재 도시에서 이동 가능한 모든 도시를 확인
    for next_city in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_city] == -1:
            # 현재 도시까지의 거리 + 1을 다음 도시의 거리로 설정
            distance[next_city] = distance[now] + 1
            # 다음 도시를 큐에 추가
            queue.append(next_city)

# 최단 거리가 k인 도시들을 result 리스트에 저장
result = [i for i in range(1, n + 1) if distance[i] == k]

# 결과 출력
if result:
    # 오름차순으로 정렬하여 출력
    for city in sorted(result):
        print(city)
else:
    # 최단 거리가 k인 도시가 없는 경우 -1 출력
    print(-1)
