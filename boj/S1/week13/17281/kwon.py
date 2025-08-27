# N이닝
# 경기가 시작하기 전까지 타순 정함, 못바꿈
# 9번 타자 치고 나면 1번 타자
# 안타, 2/3루타, 홈런, 아웃
# 타순을 정해야 함
# 4번 타자(1번 선수)는 정해져 있음
# 이닝마다 각 선수의 결과는 정해져 있음
# 가장 많은 득점을 하는 타순 찾기

from itertools import permutations

N = int(input())
hit_result = [list(map(int, input().split())) for _ in range(N)]

# # 아아아아 function call overhead !!!!!!!
# def play(order):
#     score = 0
#     idx = 0  # 타석 순서 인덱스
#     for inning in hit_result:
#         out = 0
#         base1, base2, base3 = 0, 0, 0  # 각 루의 주자 (0/1)
#         while out < 3:
#             result = inning[order[idx]]
#             if result == 0:
#                 out += 1
#             elif result == 1:
#                 score += base3
#                 base1, base2, base3 = 1, base1, base2
#             elif result == 2:
#                 score += base3 + base2
#                 base1, base2, base3 = 0, 1, base1
#             elif result == 3:
#                 score += base3 + base2 + base1
#                 base1, base2, base3 = 0, 0, 1
#             elif result == 4:
#                 score += base3 + base2 + base1 + 1
#                 base1, base2, base3 = 0, 0, 0
#             idx = (idx + 1) % 9
#     return score


max_score = 0
# permutations는 애초에 중복 없음 → set() 필요 없음
for perm in permutations([i for i in range(1, 9)]):  # 1번 선수 제외 순열
    order = list(perm[:3]) + [0] + list(perm[3:])  # 0번(1번 선수) 4번 타자 고정

    score = 0
    idx = 0  # 타석 순서 인덱스
    for inning in hit_result:
        out = 0
        base1, base2, base3 = 0, 0, 0  # 각 루의 주자 (0/1)
        while out < 3:
            result = inning[order[idx]]
            if result == 0:
                out += 1
            elif result == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif result == 2:
                score += base3 + base2
                base1, base2, base3 = 0, 1, base1
            elif result == 3:
                score += base3 + base2 + base1
                base1, base2, base3 = 0, 0, 1
            elif result == 4:
                score += base3 + base2 + base1 + 1
                base1, base2, base3 = 0, 0, 0
            idx = (idx + 1) % 9

    max_score = max(max_score, score)

print(max_score)
