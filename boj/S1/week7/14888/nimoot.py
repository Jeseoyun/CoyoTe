import itertools

n = int(input())

nums = list(map(int, input().split()))

op_tp = list(map(int, input().split()))

oper = []
for i in range(len(op_tp)):
    while op_tp[i] > 0:
        oper.append(i)
        op_tp[i] -= 1

new = set(itertools.permutations(oper, n-1))
new_list = list(new)


maxi = float('-inf')
mini = float('inf')

for opers in new_list:
    temp = nums[0]
    idx = 1
    for cal in opers:
        if cal == 0:
            temp += nums[idx]
        elif cal == 1:
            temp -= nums[idx]
        elif cal == 2:
            temp *= nums[idx]
        elif cal == 3:
            if temp < 0:
                temp *= (-1)
                temp //= nums[idx]
                temp *= (-1)
            else:
                temp //= nums[idx]
        idx += 1
    maxi = max(maxi, temp)
    mini = min(mini, temp)

print(maxi)
print(mini)