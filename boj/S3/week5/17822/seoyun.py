from collections import deque


def main():
    N, M, T = map(int, input().split())
    circles = [0] + [deque(map(int, input().split())) for _ in range(N)]
    for _ in range(T):
        # 1. x의 배수인 원판을 d 방향으로 k칸 회전
        x, d, k = map(int, input().split())
        d = -1 if d else 1

        for i in range(x, N+1, x):
            circles[i].rotate(d*(k%M))

        # 2-1. 인접 같은 수 지우기
        removed = set()
        for i in range(1, N+1):
            for j in range(M):
                if circles[i][j] == 0:
                    continue

                # 같은 원판 좌우
                if circles[i][(j-1)%M] == circles[i][j]:
                    removed.add((i, j))
                    removed.add((i, (j-1)%M))
                if circles[i][(j+1)%M] == circles[i][j]:
                    removed.add((i, j))
                    removed.add((i, (j+1)%M))

                # 상하
                if i > 1 and circles[i-1][j] == circles[i][j]:
                    removed.add((i, j))
                    removed.add((i-1, j))
                if i < N and circles[i+1][j] == circles[i][j]:
                    removed.add((i, j))
                    removed.add((i+1, j))

        if removed:
            for (i, j) in removed:
                circles[i][j] = 0

        # 2-2. 인접 같은 수 없으면 평균에서 +-1 해서 맞춰주기
        else:
            total = 0
            cnt = 0

            for i in range(1, N+1):
                for j in range(M):
                    if circles[i][j]:
                        total += circles[i][j]
                        cnt += 1

            if cnt:
                avg = total/cnt

                for i in range(1, N+1):
                    for j in range(M):
                        if circles[i][j] == 0:
                            continue

                        if circles[i][j] > avg:
                            circles[i][j] -= 1
                        elif circles[i][j] < avg:
                            circles[i][j] += 1

    print(sum(sum(c) for c in circles[1:]))


if __name__ == "__main__":
    main()