# 트럭
# https://www.acmicpc.net/problem/13335

"""
n 대의 트럭이 순서대로 다리를 건너야 함. 
다리 길이: w (트럭이 다리를 완전히 건너는데 W 시간 소요)
다리 최대 하중 : L (다리 위의 모든 트럭 무게 합이 L을 초과하면 안됨)
goal: 모든 트럭이 다리를 건넌느데 걸리는 최소 시간
"""

import sys
from collections import deque

inputf = sys.stdin.readline

def main():
    """
    트럭들이 다리를 건너는 최소 시간을 계산
    """
    n, w, l = map(int, inputf().split())  # 트럭 수, 다리 길이, 최대 하중
    trucks = list(map(int, inputf().split()))  # 각 트럭의 무게
    
    # 다리를 큐로 표현 (다리 길이만큼 0으로 초기화)
    bridge = deque([0] * w)
    
    time = 0
    current_weight = 0  # 다리 위의 현재 총 무게
    truck_index = 0  # 다음에 들어올 트럭의 인덱스
    
    while truck_index < n:  # 마지막 트럭이 다리를 완전히 건너는 시간 추가 해줘야 함
        time += 1
        
        # 다리에서 트럭이 나감 (큐의 앞에서 제거) ; 트럭이 안나갈 수 도 있음 (노상관)
        exited_weight = bridge.popleft()
        current_weight -= exited_weight
        
        # 새로운 트럭이 다리에 들어갈 수 있는지 확인
        if current_weight + trucks[truck_index] <= l:
            # 트럭이 다리에 진입
            bridge.append(trucks[truck_index])
            current_weight += trucks[truck_index]
            truck_index += 1
        else:
            # 트럭이 들어갈 수 없으면 빈 공간 추가
            bridge.append(0)
    
    # 마지막 트럭이 다리를 완전히 건너는 시간 추가
    time += w
    
    print(time)
    
    
    return


if __name__ == "__main__":
    main()
