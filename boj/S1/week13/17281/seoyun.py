def permutation(curr, used, result):
    # print(curr, used, result)
    if len(curr) == 9:
        result.append(curr[:])
        return

    if len(curr) == 3:  # 4번 타자는 무조건 1번 선수가 들어감
        used[0] = True
        permutation(curr+[0], used, result)
        return

    for num in range(9):
        if used[num]:
            continue

        used[num] = True
        permutation(curr+[num], used, result)
        used[num] = False


def main():
    N = int(input())

    player_result = []
    for _ in range(N):
        player_result.append(list(map(int, input().split())))

    # 1. 선수 순서 정하기
    player_orders = []
    used = [False for _ in range(9)]
    permutation([], used, player_orders)
    # print(player_orders)

    # 2. 점수 계산
    max_score = 0

    for inning, order in enumerate(player_orders):
        score = 0
        curr_player = 0

        out = 0
        base = [0, 0, 0]  # 1루, 2루, 3루

        while out < 3:
            player = order[curr_player]
            result = player_result[inning][player]

            if result == 0:
                out += 1
            elif result == 1:
                score += base[2]
                base[2] = base[1]
                base[1] = base[0]
                base[0] = 1
            elif result == 2:
                score += (base[2]+base[1])
                base[2] = base[0]
                base[1] = 1
                base[0] = 0
            elif result == 3:
                score += (base[2]+base[1]+1)
                base = [0, 0, 1]
            elif result == 4:
                score += base[2]+base[1]+base[0]+1

            curr_player = (curr_player+1)%9

        max_score = max(max_score, score)

    print(max_score)


if __name__ == "__main__":
    main()