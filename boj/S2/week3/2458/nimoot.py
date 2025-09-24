from collections import deque

def treeinga(num):
    global ans

    for i in range(1, n+1):
        queue_min = deque(num[i][0])  
        queue_max = deque(num[i][1]) 

        visited_min = [0] * (n+1)
        visited_max = [0] * (n+1)

        while queue_min:
            cmin = queue_min.popleft()
            
            if visited_min[cmin] == 1:
                continue

            visited_min[cmin] = 1
            for nextmin in num[cmin][0]:
                if visited_min[nextmin] == 0:
                    queue_min.append(nextmin)

        while queue_max:
            cmax = queue_max.popleft()

            if visited_max[cmax] == 1:
                continue

            visited_max[cmax] = 1
            for nextmax in num[cmax][1]:
                if visited_max[nextmax] == 0:
                    queue_max.append(nextmax)

        # 방문했던 번호들로 계산했을 때 n-1개면 위치 파악 가능
        if sum(visited_min) + sum(visited_max) == n-1:
            ans += 1

    return ans


n, m = map(int, input().split())

comp = [list(map(int, input().split())) for _ in range(m)]

num = [[[], []] for _ in range(n+1)]

for min,max in comp:
    num[min][1].append(max)  
    num[max][0].append(min)

ans = 0
print(treeinga(num))
