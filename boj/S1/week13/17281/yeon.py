# ⚾
# https://www.acmicpc.net/problem/17281

"""
    Time Out 해결 
    - list comprehension 사용 (players 초기화)
    - list.insert() 사용하지 않고 슬라이싱으로 4번 타자 자리에 1번 선수 넣기
    - base 상태를 리스트가 아닌 단순 변수로 관리
        -> 얘가 핵심, 위의 두개 설정 해놔도 50% 좀 넘어서 시간초과 발생 
        -> base 상태를 변수로 관리하니까 통과 함 
        -> index 활용한 list 삽입 삭제가 O(1) 이지만, 변수에 값을 할당하는 것보단 시간 소요가 더 크다. (by Gemini)
"""
import sys 
from itertools import permutations

inputf = sys.stdin.readline

def main():

    N = int(inputf())  # 이닝 수 (2<= N <=50)

    # for i in range(N):
    #     # 각 이닝 별 타자들의 기록
    #     # 1번 타자는 무조건 4번 타자
    #     inning = list(map(int, inputf().strip().split()))
    #     players.append(inning)    
    players = [list(map(int, inputf().strip().split())) for _ in range(N)]  # list comprehension 으로 수정 

    player_seq_list = permutations(range(1, 9), 8)  # 1번 타자 제외한 2~9번 타자들의 순열 생성
    scores = []  # 각 순열에 대한 점수를 저장할 리스트

    for player_seq in player_seq_list:  # 1번 타자를 제외한 2~9번 타자들의 순열을 순회
        player_seq = list(player_seq)  # 순열을 리스트로 변환
        # player_seq.insert(3, 0)  # 4번 타자 자리에 1번 선수(index 0) 넣어줌
        player_seq = player_seq[:3] + [0] + player_seq[3:]

        score = 0  # 현재 순열로 얻은 점수
        i = 0  # 타자 인덱스 초기화

        for inn in range(N):
            out = 0  # 현재 이닝 내 아웃 카운트
            # base = [0, 0, 0]  # 1루, 2루, 3루 상태 초기화
            base1, base2, base3 = 0, 0, 0  # 1루, 2루, 3루 상태 초기화
            while out < 3:  # 3아웃이 될 때까지 반복
                player = player_seq[i % 9]  # 현재 타자 인덱스
                hit = players[inn][player] # 현재 타자의 기록
                if hit == 0:
                    # 아웃
                    out += 1  # 아웃 카운트 증가
                elif hit == 1:
                    # 1루타
                    # score += base[2]  # 3루 주자 홈인
                    # base[2], base[1], base[0] = base[1], base[0], 1 # 타자 1루로 이동, 1루 주자 2루로, 2루 주자 3루로 이동
                    score += base3  # 3루 주자 홈인
                    base3, base2, base1= base2, base1, 1 # 타자 1루로 이동, 1루 주자 2루로, 2루 주자 3루로 이동
                elif hit == 2:
                    # 2루타
                    # score += base[2] + base[1]  # 3루, 2루 주자 홈인
                    # base[2], base[1], base[0] = base[0], 1, 0 # 1루 주자 3루로 이동, 타자 2루로 이동, 1루 비우기
                    score += base3 + base2  # 3루, 2루 주자 홈인
                    base3, base2, base1 = base1, 1, 0 # 1루 주자 3루로 이동, 타자 2루로 이동, 1루 비우기
                elif hit == 3:
                    # 3루타
                    # score += base[2] + base[1] + base[0]  # 3루, 2루, 1루 주자 홈인
                    # base[2], base[1], base[0] = 1, 0, 0  # 타자 3루로 이동, 1, 2루 비우기
                    score += base3 + base2 + base1  # 3루, 2루, 1루 주자 홈인
                    base3, base2, base1 = 1, 0, 0  # 타자 3루로 이동, 1, 2루 비우기
                else:
                    # 홈런
                    # score += 1 + sum(base)
                    # base[2], base[1], base[0] = 0, 0, 0  # 모든 베이스 비우기
                    score += 1 + base3 + base2 + base1  # 타자 홈인 + 3루, 2루, 1루 주자 홈인
                    base3, base2, base1 = 0, 0, 0  # 모든 베이스 비우기
                i += 1  # 다음 타자 

        scores.append(score)
    max_score = max(scores)  # 모든 순열 중 최대 점수 찾기

    print(max_score)  # 최대 점수 출력 

    return

if __name__=='__main__':
    main()