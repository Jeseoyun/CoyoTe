from collections import deque

def calculate(sik):
    total = 0
    num = 0
    sign = 1

    for su in sik:
        if su == ' ':
            continue
        elif su.isdigit():
            num = num * 10 + int(su)
        else:
            total += sign * num
            num = 0
            if su == '+':
                sign = 1
            else:
                sign = -1

    total += sign * num
    return total


t = int(input())

for _ in range(t):
    n = int(input())
    queue = deque()
    queue.append(("1", 2))

    while queue:
        cal, num = queue.popleft()
        
        if num > n:
            if calculate(cal) == 0:
                print(cal)
            continue
        else:
            queue.append((cal + " " + str(num), num + 1))
            queue.append((cal + "+" + str(num), num + 1))
            queue.append((cal + "-" + str(num), num + 1))

    print()
