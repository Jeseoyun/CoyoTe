from math import factorial

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    print(factorial(m) // (factorial(n) * factorial(m - n)))


#############

# 예전 DP 풀이 (어케 품?)


def dp(b1, b2, n, m):
    global memo
    if b1 == n:
        return 1
    cnt = 0
    for i in range(b2 + 1, min(m, b2 + m - n + 1) + 1):
        if (b1 + 1, i) in memo:
            cnt += memo[(b1 + 1, i)]
        else:
            tmp = dp(b1 + 1, i, n, m)
            cnt += tmp
            memo[(b1 + 1, i)] = tmp
    return cnt


t = int(input())
for _ in range(t):
    memo = {}
    n, m = map(int, input().split())
    print(dp(0, 0, n, m))
