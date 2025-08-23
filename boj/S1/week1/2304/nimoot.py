# nimoot : x의 height
# max(∞:nimoot-1], nimoot, max[nimoot+1:∞) 로 나누어서 두번째로 큰 값으로 height 설정

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
arr.sort()

total = arr[0][1] # 면적

current = 1 # 넘어가지 않은 index
left_max = arr[0][1] # 왼쪽 구간 max
right_max = max(arr[current:], key=lambda x:x[1])[1] if current < len(arr) else 0 # 오른쪽 구간 max

for x in range(arr[0][0]+1, arr[-1][0]):
    # x의 height가 0이 아니면
    if x == arr[current][0]:
        temp =  arr[current][1] # 현재 height 저장
        current += 1 # 다음 index로 이동

        left_max = max(left_max, temp) # (∞, x-1] 내 height max
        right_max = max(arr[current:], key=lambda x:x[1])[1] # [x+1, ∞) 내 height max

        # left, temp, right 중 두번째로 큰 값만 더하기
        # left, temp, right 다 더하고
        total += left_max + temp + right_max
        # 셋 중 가장 크고, 작은 값 각각 빼기
        total -= max(left_max, temp, right_max)
        total -= min(left_max, temp, right_max)
    # x의 height가 0이면
    else:
        total += min(left_max, right_max)

if T > 1: # 입력 개수가 2 이상이면 마지막 height 더하기
    total += arr[-1][1]

print(total)