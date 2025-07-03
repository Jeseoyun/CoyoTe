N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

# 집 사이 최소 거리
start = 1
# 집 사이 최대 거리
end = houses[-1] - houses[0]
result = 0

# C개의 공유기를 모두 설치할 수 있는 mid를 찾기기
while start <= end:
    mid = (start + end) // 2
    count = 1
    cur_house = houses[0]

    for i in range(1, N):
        # 현재 집과의 거리가 mid보다 크거나 같을 때 -> 설치 가능
        if houses[i] - cur_house >= mid:
            count += 1
            cur_house = houses[i]

    # 가능한 경우 더 큰 mid를 탐색
    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
