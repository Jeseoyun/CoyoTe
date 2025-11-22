# 괄호 추가하기 
# https://www.acmicpc.net/problem/16637

import sys 
inputf = sys.stdin.readline

def execute_operation(op, num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        num1 = int(num1)
        num2 = int(num2)
        
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    

def dfs(idx, current_value, numbers, operators):
    # 모든 연산자를 처리한 경우
    if idx >= len(operators):
        return current_value
    
    max_result = float('-inf')
    
    # 1. 괄호를 추가하지 않고 다음 연산 수행
    next_value = execute_operation(operators[idx], current_value, numbers[idx + 1])
    max_result = max(max_result, dfs(idx + 1, next_value, numbers, operators))
    
    # 2. 괄호를 추가하는 경우 (다음 연산자가 있을 때만)
    if idx + 1 < len(operators):
        # 다음 연산을 먼저 계산 (괄호 안)
        bracket_value = execute_operation(operators[idx + 1], numbers[idx + 1], numbers[idx + 2])
        # 현재 값과 괄호 결과를 연산
        next_value = execute_operation(operators[idx], current_value, bracket_value)
        # 괄호를 친 다음 연산자를 건너뛰고 계속 진행
        max_result = max(max_result, dfs(idx + 2, next_value, numbers, operators))
    
    return max_result
    
    
def main():
    N = int(inputf())  # 수식의 길이 
    expression = inputf().strip()  # 수식 
    
    # 숫자와 연산자 분리
    numbers = []
    operators = []
    
    for i, char in enumerate(expression):
        if i % 2 == 0:  # 숫자 위치
            numbers.append(int(char))
        else:  # 연산자 위치
            operators.append(char)
    
    # 숫자가 하나만 있는 경우
    if len(numbers) == 1:
        print(numbers[0])
        return
    
    # DFS로 최댓값 탐색
    result = dfs(0, numbers[0], numbers, operators)
    print(result)


if __name__ == "__main__":
    main()