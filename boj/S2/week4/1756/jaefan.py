# https://www.acmicpc.net/problem/1756
# 피자 굽기 

import sys 

inputf = sys.stdin.readline

def main():
    # 오븐의 깊이: D, 피자의 개수: N
    D, N = map(int, inputf().split())
    
    # 오븐의 지름 (최상단 -> 최하단)
    oven_diameters = list(map(int, inputf().split()))
    
    # 피자 반죽이 완성되는 순서에 따른 지름 
    pizza_diameters = list(map(int, inputf().split()))
    
    # 오븐 지름 전처리: 위층이 아래층보다 작으면 아래층을 위층과 같게 만듦
    # 오븐은 위에서 아래로 갈수록 지름이 작아지거나 같음
    for i in range(1, D):
        if oven_diameters[i] > oven_diameters[i-1]:
            oven_diameters[i] = oven_diameters[i-1]
    
    # 피자를 순서대로 오븐에 넣기
    current_depth = D  # 현재 오븐 깊이 (최하단 부터 시작)
    
    for pizza_diameter in pizza_diameters:
        # 현재 깊이부터 위로 올라가며 피자를 넣을 수 있는 위치 찾기
        while current_depth > 0 and oven_diameters[current_depth - 1] < pizza_diameter:
            current_depth -= 1
        
        # 피자를 넣을 수 있는 위치가 없으면
        if current_depth == 0:
            print(0)
            return
        
        # 피자를 현재 위치에 넣고 다음 피자를 위해 깊이 감소
        current_depth -= 1
    
    # 마지막 피자가 들어간 위치 출력 (1부터 시작하는 인덱스)
    print(current_depth + 1)
    return 



if __name__ == "__main__":
    main()