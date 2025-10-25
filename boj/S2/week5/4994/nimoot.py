from collections import deque

num = []

new = int(input())
while new != 0:
    num.append(new)
    new = int(input())

for n in num:
    queue = deque([(1%n, "1")])

    while queue:
        remain,cur = queue.popleft()

        if remain == 0:
            print(cur)
            break
        
        queue.append(((remain*10)%n, cur+"0"))
        queue.append(((remain*10+1)%n,cur+"1"))