# from collections import deque

# def bfs():
#     queue = deque()

#     queue.append([n])

#     while queue:
#         cur = queue.popleft()
#         # print(cur)

#         if cur[-1] == k:
#             return cur
        
#         for m in [-1,1,cur[-1]]:
#             new = cur[-1] + m
#             if 0<=new<=100000 and visited[new] == 0:
#                 queue.append(cur+[new])


# n, k = map(int, input().split())
# visited = [0] * 100001
# visited[n] = 1
# ans = bfs()
# print(len(ans)-1)
# print(*ans,end=' ')


from collections import deque

def sumbak():
    queue = deque()
    queue.append(n)
    while queue:
        current = queue.popleft()
        if current == k:
            print(visited[k])
            # print(result)
            # temp = current
            result.append(current)
            while parent[current] != -1:
                print(result)
                result.append(parent[current])
                current = parent[current]
                # print(current)
            print(*result[::-1])
            exit()
        for add in [-1,1,current]:
            new = current + add
            # if 0<= new <=100000 and visited[new] > visited[current]:
            if 0<= new <=100000 and visited[new] == -1:
                queue.append(new)
                visited[new] = visited[current] +1
                parent[new]=current


n, k = map(int, input().split())

visited = [-1] * 100001
visited[n] = 0
parent = [-1] * 100001
# parent[n] = None
result = []
sumbak()