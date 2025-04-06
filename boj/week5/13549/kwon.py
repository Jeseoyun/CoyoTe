import heapq
INF = float('inf')

N, K = map(int, input().split())
distance = [INF] * 100001

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, c = heapq.heappop(q)
        if distance[c] < dist:
            continue
        for n in (c+1, c-1, c*2):
            if n < 0 or n > 100000:
                continue

            cost = dist
            if n != c*2:
                cost = dist + 1

            if cost < distance[n]:
                distance[n] = cost
                q.append((cost, n))

dijkstra(N)
print(distance[K])