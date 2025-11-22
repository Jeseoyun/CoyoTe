INF = float('inf')


def pre_process(expressions):
    nums = []
    opers = []
    for expr in expressions:
        if expr.isdigit():
            nums.append(int(expr))
        else:
            opers.append(expr)

    return nums, opers


def calculate(a, b, op):
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == "*":
        return a*b


def dfs(idx, curr, nums, opers):
    global MAX_VAL

    if idx == len(opers):
        MAX_VAL = max(MAX_VAL, curr)
        return

    # 1. 현재 연산자 계산
    val = calculate(curr, nums[idx+1], opers[idx])
    dfs(idx+1, val, nums, opers)

    # 2. 다음 연산자 먼저 계산 후 현재꺼랑 합쳐서 계산
    if idx+1 < len(opers):
        tmp = calculate(nums[idx+1], nums[idx+2], opers[idx+1])
        val = calculate(curr, tmp, opers[idx])
        dfs(idx+2, val, nums, opers)


def main():
    global MAX_VAL

    N = int(input())
    expr = input()

    nums, opers = pre_process(expr)

    if len(opers) == 0:
        print(nums[0])
        return

    MAX_VAL = -INF
    dfs(0, nums[0], nums, opers)

    print(MAX_VAL)


if __name__ == "__main__":
    main()