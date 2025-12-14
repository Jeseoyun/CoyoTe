from collections import deque


def main():
    N, S, M = map(int, input().split())
    V = list(map(int, input().split()))

    queue = deque([(S, 0)])
    visited = [[False]*(M+1) for _ in range(N+1)]
    visited[0][S] = True

    max_vol = -1
    while queue:
        P, i = queue.popleft()

        if i == N:
            max_vol = max(max_vol, P)
            continue

        for vol in (P+V[i], P-V[i]):
            if vol < 0 or vol > M:
                continue

            if visited[i+1][vol]:
                continue

            queue.append((vol, i+1))
            visited[i+1][vol] = True

    print(max_vol)


if __name__ == "__main__":
    main()