# 0 만들기 
# https://www.acmicpc.net/problem/7490

import sys
inputf = sys.stdin.readline

def calculate(expression):
    """
    수식 문자열을 계산하는 함수
    공백을 제거하여 숫자를 이어붙인 후 계산
    예: "1 + 2" -> "1+2" 계산
        "1 2+3" -> "12+3" 계산
    """
    # 공백을 제거하여 실제 계산할 수식 생성
    expr = expression.replace(' ', '')
    
    # eval을 사용하여 수식 계산
    return eval(expr)

def dfs(n, idx, expression, results):
    """
    백트래킹을 이용한 모든 경우의 수 탐색
    
    Args:
        n: 1부터 n까지의 숫자를 사용
        idx: 현재 처리할 숫자의 인덱스 (1부터 n까지)
        expression: 현재까지 만들어진 수식 문자열
        results: 결과가 0인 수식들을 저장할 리스트
    """
    # 기저 사례: 모든 숫자를 사용한 경우
    if idx > n:
        # 수식을 계산하여 결과가 0이면 결과 리스트에 추가
        if calculate(expression) == 0:
            results.append(expression)
        return
    
    # 다음 숫자를 추가하며 재귀 호출
    # 1. 공백(' ')을 추가하는 경우: 숫자를 이어붙임
    dfs(n, idx + 1, expression + ' ' + str(idx), results)
    
    # 2. '+'를 추가하는 경우: 덧셈
    dfs(n, idx + 1, expression + '+' + str(idx), results)
    
    # 3. '-'를 추가하는 경우: 뺄셈
    dfs(n, idx + 1, expression + '-' + str(idx), results)

def main():
    tc = int(inputf())
    
    # 각 테스트 케이스 처리
    for _ in range(tc):
        N = int(inputf())
        
        # 결과를 저장할 리스트
        results = []
        
        # DFS 부시작: 첫 번째 숫자는 항상 1
        # idx=2부터 시작 (1 다음 숫자터 연산자 추가)
        dfs(N, 2, '1', results)
        
        # 결과를 사전순으로 정렬
        # 공백(' ') < '+' < '-' 순서로 자동 정렬됨
        results.sort()
        
        # 결과 출력
        for result in results:
            print(result)
        
        # 테스트 케이스 사이 빈 줄 출력
        print()

if __name__ == "__main__":
    main() 