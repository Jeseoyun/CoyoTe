# 숨바꼭질 3 
# https://www.acmicpc.net/problem/13549

# 딱 왔다. DP 구나 -> 아니네, 최단거리? BFS ?
# 예제 다른 방법 
# 5 4 8 16 17 

from collections import deque 

def main():
    UPPER = 100000
    LOWER = 0
    N, K = map(int, input().split())
    visited = set()

    def is_valid(x):
        if LOWER > x or x > UPPER or x in visited:
            return False 
        else:
            return True 

    cnt = [0 for _ in range(UPPER+1)]  # 0 <= N, K <= 100000
    qu = deque([N])
    while qu:    
        x = qu.popleft()
        if x == K:
            break
        else:
            if is_valid(2*x):
                qu.append(2*x)
                cnt[2*x] = cnt[x]  # 순간이동이므로 현재 위치와 동일한 카운트를 가짐 
                visited.add(2*x)
            if is_valid(x-1):
                qu.append(x-1)
                cnt[x-1] = cnt[x] + 1  # 한 칸 이동 
                visited.add(x-1)
            if is_valid(x+1):
                qu.append(x+1)
                cnt[x+1] = cnt[x] + 1  # 한 칸 이동
                visited.add(x+1)
    
    print(cnt[K])


if __name__=='__main__':
    main()