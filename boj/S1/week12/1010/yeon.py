# 다리 놓기 
# https://www.acmicpc.net/problem/1010

"""
    다리 놓기 -> 조합 문제 
    - 다리끼리는 교차하지 않음 
    - N <= M 이기 때문에 N개의 다리를 지음 
    - 조합 공식: nCr = n! / (r! * (n-r)!)
    - 다리의 개수 N, 기둥의 개수 M이 주어질 때,
    - M개의 기둥 중 N개의 기둥을 선택하는 경우의 수를 구함
    - 입력: 첫째 줄에 테스트 케이스의 개수 T, 다음 T줄에 N과 M이 주어짐

"""

from math import factorial

def main():
    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        if N == 0 or N == M:
            print(1)
            continue
        
        # nCr = n! / (r! * (n-r)!)
        # n = M, r = N
        
        result = factorial(M) // (factorial(N) * factorial(M - N))
        print(result)
    return

if __name__=='__main__':
    main()