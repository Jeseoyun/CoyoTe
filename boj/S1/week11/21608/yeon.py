# 상어 초등학교
# https://www.acmicpc.net/problem/21608

def main():
    N = int(input())
    
    best_friends = dict()
    adj_cond = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 인접한 칸의 조건 (상하좌우)
    order = []  # 자리 앉는 순서 

    seats = [[-1 for _ in range(N)] for _ in range(N)]  # 자리 배치

    # 기본 입력 값 
    for _ in range(N**2):
        lst = list(map(int, input().split()))
        order.append(lst[0])
        best_friends[lst[0]] = lst[1:]
        
    # print(order)  # debug
    # print(best_friends)  # debug

    for student in order:

        # 처음으로 자리를 정하는 학생의 경우 N >= 3 인 경우에 (1,1) 에 앉는다. 문제 조건에서 N >= 3 이므로 무조건 (1,1) 에 앉는다.
        if student == order[0]:
            seats[1][1] = student
            continue

        best_seat = (-1, -1)  # 자리 배치
        like_cnt = -1  # best_seat 자리 기준으로 인접한 자리에 좋아하는 학생 수 (0으로 하면 대소 비교 조건에서 문제 생김)
        empty_cnt = -1  # best_seat 자리 기준으로 인접한 자리에 비어 있는 칸 수 (0으로 하면 대소 비교 조건에서 문제 생김)

        # 자리 배치 조건 1: 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
        # 자리 배치 조건 2: 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어 있는 칸이 가장 많은 칸으로 자리를 정한다.
        # 자리 배치 조건 3: 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개 이면 열의 번호가 가장 작은 칸으로 자리를 정한다. 

        for r in range(N):
            for c in range(N):

                if seats[r][c] == -1:  # 비어 있는 칸 
                    tmp_like_cnt = 0  # (r, c) 기준으로 좋아하는 학생 수
                    tmp_empty_cnt = 0  # (r, c) 기준으로 비어 있는 칸 수

                    for dr, dc in adj_cond:
                        nr, nc = r + dr, c + dc  # 인접한 칸 좌표 

                        if 0 <= nr < N and 0 <= nc < N: # 유효성 검사 (is_valid)
                            if seats[nr][nc] in best_friends[student]:  # 인접한 칸에 좋아하는 학생이 있는 경우
                                tmp_like_cnt += 1  # 좋아하는 학생 수 증가

                            elif seats[nr][nc] == -1:  # 인접한 칸이 비어 있는 경우
                                tmp_empty_cnt += 1  # 비어 있는 칸 수 증가
                        
                    if tmp_like_cnt > like_cnt:  # 현재 자리 기준으로 인접한 자리에 좋아하는 학생 수가 더 많은 경우
                        like_cnt = tmp_like_cnt
                        empty_cnt = tmp_empty_cnt
                        best_seat = (r, c)

                    elif tmp_like_cnt == like_cnt:  # 현재 자리 기준으로 인접한 자리에 좋아하는 학생 수가 같은 경우
                        if tmp_empty_cnt > empty_cnt:  # 현재 자리 기준으로 인접한 자리에 좋아하는 학생의 수가 동일하고, 비어 있는 칸의 수가 더 많은 경우
                            like_cnt = tmp_like_cnt
                            empty_cnt = tmp_empty_cnt
                            best_seat = (r, c)

                        elif tmp_empty_cnt == empty_cnt:  # 현재 자리 기준으로 인접한 자리에 존재하는 학생의 수가 동일하고, 비어 있는 칸의 개수가 동일한 경우 
                            if r < best_seat[0]:  # 행의 번호가 더 작은 경우
                                like_cnt = tmp_like_cnt
                                empty_cnt = tmp_empty_cnt
                                best_seat = (r, c)

                            elif r == best_seat[0]:  # 행의 번호가 동일한 경우
                                if c < best_seat[1]:
                                    like_cnt = tmp_like_cnt
                                    empty_cnt = tmp_empty_cnt
                                    best_seat = (r, c)
                                continue 
                else: 
                    continue
        
        # 자리 배치 
        # print(f"학생 {student} 의 자리 배치: {best_seat}")  # debug
        seats[best_seat[0]][best_seat[1]] = student

    # print(seats)  # debug

    # 자리 배치 만족도 설문 
    # 점수 기준: 인접한 자리에 좋아하는 학생의 수에 따라서 0: 0점, 1: 1점, 2: 10점, 3: 100점, 4: 1000점
    score = 0
    for r in range(N):
        for c in range(N):
            like_cnt = 0
            for dr, dc in adj_cond:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and seats[r][c] != -1: # 유효성 검사 (is_valid)
                    if seats[nr][nc] in best_friends[seats[r][c]]:  # 인접한 칸에 좋아하는 학생이 있는 경우
                        like_cnt += 1  # 좋아하는 학생 수 증가
            
            # 점수 부여
            if like_cnt == 0:
                score += 0
            elif like_cnt == 1:
                score += 1
            elif like_cnt == 2:
                score += 10
            elif like_cnt == 3:
                score += 100
            elif like_cnt == 4:
                score += 1000

    print(score)  # 최종 결과 

    return 


if __name__=='__main__':
    main()