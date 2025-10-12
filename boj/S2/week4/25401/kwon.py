# BOJ 25401 카드 바꾸기

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

ans = n - 2

# 모든 가능한 두 카드 조합 (i, j)에 대해 확인
for i in range(n):
    for j in range(i + 1, n):
        if (cards[j] - cards[i]) % (j - i) != 0:
            continue
        d = (cards[j] - cards[i]) // (j - i)
        cnt = 0
        
        for k in range(n):
            expected = cards[i] + (k - i) * d
            if cards[k] != expected:
                cnt += 1
        
        ans = min(ans, cnt)

print(ans)