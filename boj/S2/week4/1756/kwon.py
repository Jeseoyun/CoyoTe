# 1756 피자 굽기
import sys
input = sys.stdin.readline

D, N = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))

min_oven = oven[0]
for i in range(1, D):
    min_oven = min(min_oven, oven[i])
    oven[i] = min(oven[i], min_oven)

oven_i = D - 1
dough_i = 0

while dough_i < N:
    # print(oven_i, dough_i)
    if oven[oven_i] < doughs[dough_i]:
        # 못들어감
        oven_i -= 1
        if oven_i < 0:
            # 다 들어갈 수 없음
            print(0)
            break
    else:
        dough_i += 1
        oven_i -= 1

else:
    print(oven_i + 2)
