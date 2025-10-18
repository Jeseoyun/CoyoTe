# https://www.acmicpc.net/problem/25401
# 카드 바꾸기 

## 일정하게 증가하거나, 일정하게 감소하거나 혹은 모두 동일하게 만들기 위한 카드 숫자 변경 최소 횟수 

import sys 

inputf = sys.stdin.readline

def main():
    # 입력: N개의 카드 숫자
    N = int(inputf())
    cards = list(map(int, inputf().split()))
    
    # 예외 처리: 카드가 2개 이하인 경우 변경할 필요 없음
    if N <=2 :
        print(0)
        return
    
    # 최소 변경 횟수를 저장할 변수 (최악의 경우 모든 카드 변경)
    min_changes = N
    
    # 핵심 아이디어: 임의의 두 위치를 선택하여 그 값들을 유지하고 등차수열을 만듦
    # 모든 가능한 두 위치의 조합을 시도 (O(N^2))
    for i in range(N):
        for j in range(N):
            # 같은 위치는 건너뛰기 
            if i == j:
                continue
            
            # 등차수열의 공차 계산
            # 공차 = (두 번째 값 - 첫 번째 값) / (두 번째 위치 - 첫 번째 위치)
            # 공차가 정수가 아니면 유효한 등차수열을 만들 수 없음
            if (cards[j] - cards[i]) % (j - i) != 0:
                continue  # 정수 공차가 아니면 이 조합은 불가능 -> 건너뛰기 
            
            # 정수 공차 계산
            d = (cards[j] - cards[i]) // (j - i)
            
            # 등차수열의 첫 항 계산 (위치 0에서의 값)
            # 위치 i에서의 값이 cards[i]이므로, 위치 0에서의 값은 cards[i] - d * i
            first_value = cards[i] - d * i
            
            # 현재 카드 배열에서 변경하지 않아도 되는 카드의 개수 계산
            keep_count = 0
            for k in range(N):
                # 위치 k에서 예상되는 값 계산
                expected = first_value + d * k
                # 현재 카드의 값이 예상값과 같으면 변경할 필요 없음
                if cards[k] == expected:
                    keep_count += 1
            
            # 변경해야 하는 카드 수 = 전체 카드 수 - 유지할 수 있는 카드 수
            changes = N - keep_count
            # 최소 변경 횟수 갱신
            min_changes = min(min_changes, changes)
    
    # 최소 변경 횟수 출력
    print(min_changes)
    return 
    
if __name__ == "__main__":
    main()