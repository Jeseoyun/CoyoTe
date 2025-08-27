def main():
    N, d, k, c = map(int, input().split())  # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
    sushi_go_round = [int(input()) for _ in range(N)]

    max_kind_of_sushi = 0
    for start in range(N):
        sushi_seq = [sushi_go_round[i%N] for i in range(start, start + k)]  # 회전하므로 범위 넘어가면 0번부터 다시 시작
        unique_sushi = set(sushi_seq)

        bonus = 1 if c not in unique_sushi else 0  # 연속된 4개 중 보너스 초밥이 없을 경우 +1 해준다

        max_kind_of_sushi = max(max_kind_of_sushi, len(unique_sushi) + bonus)

    print(max_kind_of_sushi)


if __name__ == "__main__":
    main()