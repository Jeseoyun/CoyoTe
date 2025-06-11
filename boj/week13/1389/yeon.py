# 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
from collections import deque 

inputf = sys.stdin.readline

def bfs(start, graph):
    visited = [False] * (len(graph))  # 방문 여부를 저장할 리스트
    queue = deque([start])  # BFS를 위한 큐 초기화
    visited[start] = True  # 시작 노드 방문 처리
    distances = [0 for _ in range(len(graph))]  # 시작 노드와의 거리 초기화
    while queue:
        current = queue.popleft()  # 큐에서 현재 노드 꺼내기
        for neighbor in graph[current]:  # 현재 노드의 이웃 노드들 탐색
            if not visited[neighbor]:  # 이웃 노드가 방문되지 않았다면
                visited[neighbor] = True  # 방문 처리
                queue.append(neighbor)  # 큐에 추가
                distances[neighbor] += distances[current] + 1  # 거리 증가
    
    # print(f"Start: {start}, Distances: {distances}")  # 디버깅용 출력
    return distances  # BFS를 통해 계산된 거리 반환


def find_kevin_bacon(graph):
    min_distance = float('inf')  # 최소 거리를 무한대로 초기화
    kevin_bacon_number = -1  # 케빈 베이컨 번호 초기화

    for person in range(1, len(graph)):  # 사람 번호는 1부터 시작하므로 1부터 N까지 반복
        distance = sum(bfs(person, graph))  # BFS를 통해 현재 사람의 케빈 베이컨 수 계산
        if distance < min_distance:  # 현재 사람이 더 작은 거리를 가지면
            min_distance = distance  # 최소 거리 갱신
            kevin_bacon_number = person  # 케빈 베이컨 번호 갱신
            # 번호가 작은 사람에서 큰 사람으로 진행되므로, if 의 조건을 less than (<) 으로 설정 

    return kevin_bacon_number  # 최종적으로 케빈 베이컨 번호 반환


def main():
    N, M = map(int, inputf().strip().split())  # N: 사람 수, M: 관계 수
    graph = [[] for _ in range(N+1)]  # 사람 번호는 1부터 시작하므로 N+1 크기의 리스트 생성

    # 관계를 그래프로 표현 (인접행렬)
    for _ in range(M):
        a, b = map(int, inputf().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    # 케빈 베이컨의 수가 가장 작은 사람 찾기
    result = find_kevin_bacon(graph)
    print(result)  # 결과 출력

    return

if __name__=='__main__':
    main()