# trial 1. bfs로 탐색할 수 있는 놈이 가장 많은걸 찾으면 되겠군
# => 메모리 초과 -> 시간 초과 -> 메모리 초과 -> 시간 초과 -> ...

# trial 2. 아하! 가장 긴놈의 대가리만 찾으면 가장 많은 컴퓨터를 한 번에 해킹할 수 있겠군
# => 진입 차수 0인 놈들 찾아서 bfs로 길이 알아낸 뒤에 가장 긴 놈 출력하자
# => but 간과한 점. 하나의 노드에서 뻗어나온 개수 자체가 많을 수도 있으므로 그래프 길이로 판단하면 안된다. 길이가 긴 놈이 아니라 영역이 큰 놈을 찾아야 함.
#   1>2>3 보다 1>2/1>3/1>4/1>5가 더 많이 해킹할 수 있다

# trial 3. 음... 이미 탐색한 놈은 한 번 더 탐색하면 안되겠군
# => 이거 BFS에서 visited 공유할 수 있나?
# => 복잡하네 ;; DFS + 메모이제이션으로 간다
# => Recursion Error ;;;;;

# trial 4. D는 포기다. B로 가고 내가 할 수 있는 방법 총 동원한다


# from collections import deque
#
#
# def bfs(graph, start):
#     queue = deque()
#     visited = set()
#     cnt = 1
#
#     queue.append(start)
#     visited.add(start)
#
#     while queue:
#         curr = queue.popleft()
#         for neighbor in graph[curr]:
#             if neighbor in visited:
#                 continue
#             queue.append(neighbor)
#             visited.add(neighbor)
#             cnt += 1
#
#     return cnt
#
#
# def dfs(curr, graph, hacked, visited):
#     if hacked[curr] != -1:
#         return hacked[curr]
#
#     if curr in visited:
#         return 0
#
#     visited.add(curr)
#     count = 1
#
#     for neighbor in graph[curr]:
#         count += dfs(neighbor, graph, hacked, visited)
#
#     visited.remove(curr)
#     hacked[curr] = count
#     return count
#
#
# def main():
#     N, M = map(int, input().split())
#     connected = {i: [] for i in range(1, N+1)}
#
#     for _ in range(M):
#         A, B = map(int, input().split())
#         connected[B].append(A)  # B를 해킹하면 A도 해킹
#     # print(connected)
#
#     hacked = {i: -1 for i in range(1, N+1)}
#     max_count = 0
#     max_connected = []
#     for node in connected.keys():
#         if hacked[node] != -1:
#             curr_cnt = hacked[node]
#         else:
#             curr_cnt = dfs(node, connected, hacked)
#
#         if curr_cnt > max_count:
#             max_count = curr_cnt
#             max_connected = [node]
#         elif curr_cnt == max_count:
#             max_connected.append(node)
#
#     print(" ".join(map(str, max_connected)))
#
#
# if __name__ == "__main__":
#     main()


##################################################### 최종 제출본
# 알게된 점
# 1. 그래프를 딕셔너리로 만드는 것 보다 인접리스트 형식으로 만들 때 접근 속도가 더 빠름
# -> 리스트는 연속된 메모리 공간에 데이터를 저장하기 때문. 딕셔너리나 집합은 해시 테이블 기반이라 약간의 오버헤드 발생
# 2. sys.stdin.readline을 적극 도입하여 사용하자

import sys
from collections import deque

input = sys.stdin.readline


def count_hackable(start, graph):
    visited = [False] * len(graph)
    visited[start] = True
    queue = deque([start])
    count = 1  # 자기 자신 포함

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count


def main():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[B].append(A)  # B를 해킹하면 A도 해킹할 수 있음

    max_count = 0
    counts = [0] * (N + 1)

    for i in range(1, N + 1):
        counts[i] = count_hackable(i, graph)
        max_count = max(max_count, counts[i])

    result = []
    for i in range(1, N + 1):
        if counts[i] == max_count:
            result.append(i)

    print(*result)


if __name__ == "__main__":
    main()