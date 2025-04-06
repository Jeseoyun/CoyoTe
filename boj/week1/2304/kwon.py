N = int(input())

max_h = 0
pillar_list = [0] * 1001

max_loc = 0
for _ in range(N):
    loc, h = map(int, input().split())
    max_h = max(max_h, h)
    max_loc = max(max_loc, loc)
    pillar_list[loc] = h

# 왼쪽에서 시작
i_l = -1
cur = 0
ans = 0
while cur < max_h:
    i_l += 1
    cur = max(cur, pillar_list[i_l])
    ans += cur

# 오른쪽에서 시작
i_r = max_loc + 1
cur = 0
while cur < max_h:
    i_r -= 1
    cur = max(cur, pillar_list[i_r])
    ans += cur

if i_r == i_l:
    ans -= max_h
else:
    ans += max_h * (i_r - i_l - 1)

print(ans)