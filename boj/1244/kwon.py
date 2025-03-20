def toggle_switch(switches, N, gender, num):
    if gender == 1:
        # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
        for i in range(num - 1, N, num):
            switches[i] = (switches[i] + 1) % 2
    else:
        # 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
        num -= 1
        switches[num] = (switches[num] + 1) % 2

        i = 1
        while num - i >= 0 and num + i < N:
            if switches[num - i] != switches[num + i]:
                break

            switches[num - i] = (switches[num - i] + 1) % 2
            switches[num + i] = (switches[num + i] + 1) % 2
            i += 1
    return switches

N = int(input())
switches = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())
    switches = toggle_switch(switches, N, gender, num)

for i in range(N // 20 + 1):
    print(*switches[i*20:(i + 1)*20])

##################

def boy(k):
    mul = num//k
    for dex in range(1, mul+1):
        arr[dex*k] = (arr[dex*k] + 1) % 2


def girl(k):
    change = [k]
    start = 1
    while 1<= k-start and k+start <= num and arr[k-start] == arr[k+start]:
        change.append(k-start)
        change.append(k+start)
        start += 1
    for ind in change:
        arr[ind] = (arr[ind] + 1) % 2



num = int(input())
arr = [5]
if num % 20 == 0:
    rou = num // 20
else:
    rou = num // 20 + 1


temp = list(map(int, input().split()))
arr += temp

stud = int(input())
for _ in range(stud):
    gen, swi = map(int, input().split())

    if gen == 1:#남자
        boy(swi)
    else:#여자
        girl(swi)

for idx in range(1, num+1):
    print(arr[idx], end=' ')
    if idx % 20 == 0:
        print()