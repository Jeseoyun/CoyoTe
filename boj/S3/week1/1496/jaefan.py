# 기타리스트
# https://www.acmicpc.net/problem/1495


import sys 
inputf = sys.stdin.readline

def main():
    N, S, M = map(int, inputf().split())
    V = list(map(int, inputf().split()))
    
    current_volumees = set([S])  # 현재 가능한 볼륨 집합
    
    
    for v in V:
        new_volumees = set()  # 볼륨 조정 후 가능한 볼륨 집합
        for volume in current_volumees:
            if volume - v >= 0:  # 조건 만족
                new_volumees.add(volume - v)  
            if volume + v <= M:  # 조건 만족
                new_volumees.add(volume + v)
        current_volumees = new_volumees
    
    if current_volumees:
        print(max(current_volumees))  # 가능한 볼륨 중 최대값 출력
    else:
        print(-1)  # 가능한 볼륨이 없으면 -1 출력
    return 

if __name__ == "__main__":
    main()