from collections import deque
import heapq

def nag_int(s):
    """음수 정수를 반환"""
    return -int(s)

TC = int(input())
for t in range(TC):
    N, M = map(int, input().split())
    importance_list = list(map(nag_int, input().split()))
    q = deque([(i, im) for i, im in enumerate(importance_list)])
    heapq.heapify(importance_list)

    cnt = 1
    cur_min = heapq.heappop(importance_list)

    while q:
        i, im = q.popleft()
        if i == M and cur_min == im:
            # M 번째 출력되면 끝
            break
        elif cur_min == im:
            # 출력 가능하면 다음으로
            cur_min = heapq.heappop(importance_list)
            cnt += 1
        else:
            # 출력 안되면 대기열 맨 뒤로
            q.append((i, im))
    print(cnt)


#################################################################
# 2년 전 풀이

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    order = list(range(n))
    cnt = 0
    while q:
        cur = q.pop(0)
        cur_order = order.pop(0)
        cnt += 1

        for i, num in enumerate(q):
            if num > cur:
                q.append(cur)
                tmp_q = q[:i]
                q = q[i:] + tmp_q
                order.append(cur_order)
                tmp_order = order[:i]
                order = order[i:] + tmp_order
                cur_order = -1
                cnt -= 1
                break
        if cur_order == m:
            break
    print(cnt)