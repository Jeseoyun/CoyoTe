import heapq
from collections import defaultdict

INF = float('inf')


def dijkstra(graph, start):
    dist = {node: INF for node in graph.keys()}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)

        for neighbor in graph[curr_node]:
            if dist[neighbor] > curr_dist + 1:
                dist[neighbor] = curr_dist + 1
                heapq.heappush(heap, (curr_dist + 1, neighbor))

    return dist


def main():
    N, M = map(int, input().split())
    friends = defaultdict(set)  # 친구 관계 중복 발생 가능성

    for _ in range(M):
        A, B = map(int, input().split())
        friends[A].add(B)
        friends[B].add(A)  # 양방향 연결

    min_kevin_bacon = INF
    min_kevin_bacon_person = ''

    for person in range(1, N+1):
        dist = dijkstra(friends, person)
        kevin_bacon = sum(dist.values())

        if min_kevin_bacon > kevin_bacon:
            min_kevin_bacon = kevin_bacon
            min_kevin_bacon_person = person

    print(min_kevin_bacon_person)


if __name__ == "__main__":
    main()