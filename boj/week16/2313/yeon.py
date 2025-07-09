# 보석 구매하기 
# https://www.acmicpc.net/problem/2313

import sys

inputf = sys.stdin.readline

def main():
    n = int(inputf())

    total_max_value = 0
    final_indices = []

    for _ in range(n):
        l = int(inputf())
        jewels = list(map(int, inputf().rstrip().split()))

        # 각 줄마다 사용할 변수 초기화 (0-based 인덱스 사용)
        global_max = -float('inf')
        current_max = 0
        
        start = 0       # 최종 시작 인덱스
        end = 0         # 최종 끝 인덱스
        temp_start = 0  # 현재 부분합의 시작 인덱스

        for i in range(l):
            # 현재 부분합이 0 이하면, 새로 시작하는 것이 이득
            if current_max <= 0:
                current_max = jewels[i]
                temp_start = i
            else:
                current_max += jewels[i]

            # global_max 갱신 조건 확인
            # 1. 새로운 최대값이 나타났을 때
            if current_max > global_max:
                global_max = current_max
                start = temp_start
                end = i
            # 2. 최대값은 같지만, 구간 길이가 더 짧을 때
            elif current_max == global_max:
                if (i - temp_start) < (end - start):
                    start = temp_start
                    end = i
        
        total_max_value += global_max
        # 최종 출력 시에만 1-based 인덱스로 변환
        final_indices.append((start + 1, end + 1))

    print(total_max_value)
    for s, e in final_indices:
        print(s, e)

if __name__ == '__main__':
    main()