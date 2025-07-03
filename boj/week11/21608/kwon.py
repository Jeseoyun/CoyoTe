N = int(input())

class_room = [[0] * N for _ in range(N)]
like_list = [[] for _ in range(N ** 2 + 1)]
students = [list(map(int, input().split())) for _ in range(N ** 2)]
for s in students:
    like_list[s[0]] = s[1:]

dij = ((-1, 0), (1, 0), (0, -1), (0, 1))

def find_seat(n):
    like = like_list[n]
    max_pref = []
    
    for i in range(N):
        for j in range(N):
            if class_room[i][j] != 0:
                continue

            like_cnt = 0
            empty_cnt = 0

            for di, dj in dij:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if class_room[ni][nj] in like:
                        like_cnt += 1
                    elif class_room[ni][nj] == 0:
                        empty_cnt += 1

            max_pref.append(( -like_cnt, -empty_cnt, i, j))

    max_pref.sort()
    x, y = max_pref[0][2], max_pref[0][3]
    class_room[x][y] = n

def calc_score():
    score = 0
    point = [0, 1, 10, 100, 1000]

    for i in range(N):
        for j in range(N):
            cnt = 0
            n = class_room[i][j]
            like = like_list[n]
            for di, dj in dij:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if class_room[ni][nj] in like:
                        cnt += 1
            score += point[cnt]
    return score

for student in students:
    find_seat(student[0])

print(calc_score())
