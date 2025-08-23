def boy(k):
    mul = num//k
    for dex in range(1, mul+1):
        arr[dex*k] = (arr[dex*k] + 1) % 2
    # start = k
    # while start <= num:
    #     arr[start] = (arr[start] + 1) % 2
    #     start += k


def girl(k):
    change = [k]
    start = 1
    while True:
        if 1 <= k-start and k+start <= num and arr[k-start] == arr[k+start]:
            change.append(k-start)
            change.append(k+start)
            start += 1
        else:
            break
    for ind in change:
        arr[ind] = (arr[ind] + 1) % 2


num = int(input())
arr = [5]
# if num % 20 == 0:
#     rou = num // 20
# else:
#     rou = num // 20 + 1

# print(rou)

# for _ in range(rou):
temp = list(map(int, input().split()))
arr += temp

# print(arr)

dent = int(input())
for _ in range(dent):
    gen, swi = map(int, input().split())

    if gen == 1:#남자
        boy(swi)
    else:#여자
        girl(swi)
    # print(arr)

for idx in range(1, num+1):
    print(arr[idx], end=' ')
    if idx % 20 == 0:
        print()