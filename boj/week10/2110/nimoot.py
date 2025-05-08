def can_place(houses, c, dist):
    count = 1  # 첫 번째 집에는 공유기를 항상 설치
    last_pos = houses[0]  # 마지막으로 공유기를 설치한 위치

    for i in range(1, len(houses)):
        # 현재 집과 마지막 설치 위치 사이의 거리가 dist 이상이면 설치
        if houses[i] - last_pos >= dist:
            count += 1
            last_pos = houses[i]
    
    # c개 이상의 공유기를 설치할 수 있는지 여부 반환
    return count >= c

# 집의 개수 n, 공유기 개수 c 입력 받기
n, c = map(int, input().split())

# n개의 집 위치 입력 받기
houses = [int(input()) for _ in range(n)]
houses.sort()  # 오름차순 정렬

# 가능한 거리 범위 설정
left = 1  # 최소 거리
right = houses[-1] - houses[0]  # 최대 거리
answer = 0

# 이진 탐색으로 최적의 거리 찾기
while left <= right:
    mid = (left + right) // 2  # 현재 거리 후보
    if can_place(houses, c, mid):
        answer = mid  # 더 넓은 거리도 가능할 수 있으므로 시도
        left = mid + 1
    else:
        right = mid - 1  # 거리를 줄여서 다시 시도

# 결과 출력
print(answer)
