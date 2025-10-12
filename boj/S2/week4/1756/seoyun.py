def main():
    D, N = map(int, input().split())  # 오븐 깊이, 피자 반죽 개수
    oven = list(map(int, input().split()))
    pizza = list(map(int, input().split()))

    # 오븐 다음 칸이 더 크더라도 위가 좁으면 더 내려갈 수 없음
    for i in range(1, D):
        if oven[i] > oven[i-1]:
            oven[i] = oven[i-1]

    pos = D - 1

    for p in pizza:
        placed = False
        for idx in range(pos, -1, -1):  # pos부터 위로 탐색
            if oven[idx] >= p:
                pos = idx - 1
                placed = True
                break

        if not placed:
            print(0)
            return

    print(pos+2)  # 마지막 피자 위치 + 1


if __name__ == "__main__":
    main()