class Ladder:
    def __init__(self, N, M, H):
        self.ladder = [[0]*N for _ in range(H)]
        self.extra = 4

        for _ in range(M):
            x, y = map(int, input().split())
            self.ladder[x-1][y-1] = 1

    def check(self, N, H):
        '''
        i번 사다리가 i번 결과에 도착하는지 확인
        '''
        for j in range(N):  # 사다리 출발점
            now = j
            for i in range(H):
                if self.ladder[i][now]:  # 오른쪽 선 이동
                    now += 1
                elif now > 0 and self.ladder[i][now-1]:  # 왼쪽 선
                    now -= 1

            # 끝까지 도달했을 때 시작지점과 불일치
            if now != j:
                return False

        return True

    def build(self, N, H, x, y, extra):
        '''
        사다리 놓기
        '''
        if self.check(N, H):
            self.extra = min(self.extra, extra)
            return

        elif extra == 3 or self.extra <= extra:
            return

        for i in range(x, H):
            if i == x:  # 행이 변경되기 전
                now = y
            else:  # 행이 변경되면 처음부터 탐색
                now = 0

            for j in range(now, N-1):
                # 사다리 못놓는 경우: 이미 1이거나, 왼쪽 or 오른쪽이 이미 1일 때
                if self.ladder[i][j] or self.ladder[i][j-1] or self.ladder[i][j+1]:
                    continue

                self.ladder[i][j] = 1
                self.build(N, H, i, j, extra+1)
                self.ladder[i][j] = 0


def main():
    N, M, H = map(int, input().split())
    ladder = Ladder(N, M, H)
    ladder.build(N, H, 0, 0, 0)

    print(ladder.extra if ladder.extra < 4 else -1)


if __name__ == "__main__":
    main()