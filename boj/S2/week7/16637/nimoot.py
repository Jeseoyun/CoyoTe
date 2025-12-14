from collections import deque

n = int(input())
susik = input()

nums = []
ops = []

for i in range(n):
    if i % 2 == 0:
        nums.append(int(susik[i]))
    else:
        ops.append(susik[i])

def calc(a, op, b):
    if op == '+': 
        return a + b
    elif op == '-': 
        return a - b
    else:
        return a * b

ans = float('-inf')

queue = deque()
queue.append((nums[0], 0))

while queue:
    current, idx = queue.popleft()

    if idx == len(ops):
        ans = max(ans, current)
        continue

    cal1 = calc(current, ops[idx], nums[idx + 1])
    queue.append((cal1, idx + 1))

    if idx + 1 < len(ops):
        temp = calc(nums[idx + 1], ops[idx + 1], nums[idx + 2])
        cal2 = calc(current, ops[idx], temp)
        queue.append((cal2, idx + 2))

print(ans)
