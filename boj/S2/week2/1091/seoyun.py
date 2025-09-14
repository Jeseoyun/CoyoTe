def shuffle(current, N, S):
    shuffled = [0] * N
    for i in range(N):
        shuffled[i] = current[S[i]]
    return shuffled


def main():
    N = int(input())
    P = list(map(int, input().split()))  # 목표
    S = list(map(int, input().split()))  # 카드 섞기

    current = [i for i in range(N)]
    original = current[:]

    cnt = 0

    while True:
        if [card%3 for idx, card in enumerate(current)] == P:
            print(cnt)
            break

        current = shuffle(current, N, S)
        # print(current)

        if current == original:
            print(-1)
            break

        cnt += 1


if __name__ == "__main__":
    main()