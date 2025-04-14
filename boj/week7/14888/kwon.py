operate = ['+', '-', '*','/']

N = int(input())
nums = list(map(int, input().split()))
operator_counter = list(map(int, input().split()))
operator_cnt = sum(operator_counter)

max_com = -float('inf')
min_com = float('inf')


def compute(a, b, op_i):
    if op_i == 0:
        return a + b
    elif op_i == 1:
        return a - b
    elif op_i == 2:
        return a * b
    elif op_i == 3:
        return int(a / b)

def dfs(operator_counter, result, n=0):
    global max_com, min_com
    if n == operator_cnt:
        max_com = max(max_com, result)
        min_com = min(min_com, result)
        return
    for i, cnt in enumerate(operator_counter):
        if cnt == 0:
            continue
        operator_counter[i] -= 1
        dfs(operator_counter, compute(result, nums[n+1], i), n+1)
        operator_counter[i] += 1


dfs(operator_counter, nums[0])

print(max_com)
print(min_com)