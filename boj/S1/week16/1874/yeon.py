# 스택 수열
# https://www.acmicpc.net/problem/1874

import sys 
from collections import deque 

inputf = sys.stdin.readline

def main():

    n = int(inputf())

    stack = [int(inputf()) for _ in range(n)]  # 문제에서 주어진 스택 
    
    tmp_stack = list()  # 만들어갈 스택 
    ops = list()  # push, pop 연산 저장 리스트 

    cnt = 1  # 스택에 넣을 숫자, 1부터 시작 
    for num in stack:  # 주어진 스택 숫자 순회 
        while cnt <= num:  # 스택에 넣을 숫자가 주어진 숫자보다 작거나 같은 경우
            tmp_stack.append(cnt)  # push 
            ops.append("+")  # push 연산 저장 
            cnt += 1  # 숫자 증가 
        
        if tmp_stack and tmp_stack[-1] == num:  # 스택의 마지막 숫자가 주어진 숫자와 같은 경우 
            tmp_stack.pop()  # pop 
            ops.append("-")  # pop 연산 저장 

        else:  # 스택의 마지막 숫자가 주어진 숫자와 다른 경우 -> 수열을 만들지 못함. 
            # (해당 숫자보다 작거나 같은 숫자를 모두 push 했지만 pop 하는 순간 주어진 수열의 숫자가 나오지 않음 )
            print("NO")
            return 
    
    print(*ops, sep="\n")  # 연산 결과 출력
            
    return

if __name__=='__main__':
    main()