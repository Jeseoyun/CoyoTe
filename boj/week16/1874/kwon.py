n = int(input())

cur_num = 2
stack = [1]
result = ['+']
for _ in range(n):
    target = int(input())
    if not stack:
        stack.append(cur_num)
        result.append('+')
        cur_num += 1
    while stack and stack[-1] < target:
        stack.append(cur_num)
        result.append('+')
        cur_num += 1
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
        continue

if len(stack) == 0:
    print(*result, sep='\n')
else:
    print('NO')