from collections import Counter

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

count_dict = Counter(arr)

num_set = sorted(set(arr))
num_double_set=set(arr)

leng = len(num_set)
ans = [0]*leng

sorted_items = sorted(count_dict.items())

cnt = [[0, 0] for _ in range(1000001)]

for i in range(leng):
    cnt[sorted_items[i][0]][0]=sorted_items[i][0]
max_num = sorted_items[-1][0]

for idx in range(leng):
    base = num_set[idx]
    cnt[base][1] += sorted_items[idx][1]-1

    for comp in range(base*2,max_num+1,base):
        if comp in num_double_set and cnt[comp][0] % sorted_items[idx][0] == 0:
            cnt[comp][1] += sorted_items[idx][1]

for value in arr:
    print(cnt[value][1])
