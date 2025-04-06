from collections import deque


MAX = 100001  # 100000도 포함해야함...


def main():
    N, K = map(int, input().split())
    visited = [-1] * MAX  # 각 위치까지 걸리는 시간
    visited[N] = 0

    queue = deque()
    queue.append(N)

    while queue:
        curr = queue.popleft()

        if curr == K:
            print(visited[curr])  # 가장 먼저 도달했을 때가 최소 시간!
            return

        for next in (curr*2, curr-1, curr+1):
            if next < 0 or next > MAX or visited[next] != -1:
                continue
            if next == curr * 2:  # 순간이동(0초)
                visited[next] = visited[curr]
            else:
                visited[next] = visited[curr] + 1

            queue.append(next)


if __name__ == "__main__":
    main()