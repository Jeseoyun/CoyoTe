def dfs(now, n, expression, current_sum, last_number):
    
    if now == n:
        if current_sum + last_number == 0:
            print(expression)
        return

    next_number = now + 1

    # ASCII 순서: ' ' (공백) -> '+' (더하기) -> '-' (빼기)

    if last_number > 0:
        new_last = last_number * 10 + next_number
    else:
        new_last = last_number * 10 - next_number
        
    dfs(next_number, n, expression + f" {next_number}", current_sum, new_last)
    dfs(next_number, n, expression + f"+{next_number}", current_sum + last_number, next_number)
    dfs(next_number, n, expression + f"-{next_number}", current_sum + last_number, -next_number)

def solve():
    t = int(input())
    
    for _ in range(t):
        num = int(input())
        # 현재 = 1, 목표 = num, 수식 = "1", 현재합 = 0, 마지막숫자 = 1
        dfs(1, num, "1", 0, 1)
        print()

if __name__ == "__main__":
    solve()