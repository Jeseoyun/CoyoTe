# 16637 괄호 추가하기
class Calculator:
    def __init__(self, n, expression):
        self.n = n
        self.expression = expression
        self.max_result = float('-inf')

    @staticmethod
    def _execute(op, num1, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2

    def dfs(self, idx, current_result):
        if idx >= self.n:
            self.max_result = max(self.max_result, current_result)
            return

        # 현재 연산자를 괄호 없이 처리
        op = self.expression[idx - 1]
        num = int(self.expression[idx])
        self.dfs(idx + 2, Calculator._execute(op, current_result, num))

        # 괄호를 적용하여 처리
        if idx + 2 < self.n:
            next_op = self.expression[idx + 1]
            next_num = int(self.expression[idx + 2])
            bracket_result = Calculator._execute(next_op, num, next_num)
            self.dfs(idx + 4, Calculator._execute(op, current_result, bracket_result))

    def solve(self):
        # 첫 번째 숫자를 초기값으로 설정하고 DFS 시작
        self.dfs(2, int(self.expression[0]))
        return self.max_result


if __name__ == "__main__":
    n = int(input())
    expression = input().strip()
    calculator = Calculator(n, expression)
    print(calculator.solve())
