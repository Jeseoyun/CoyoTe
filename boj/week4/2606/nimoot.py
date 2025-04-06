node = int(input())

arr = list([i] for i in range(node+1))
# print(arr)

line = int(input())

for _ in range(line):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

link = [1]

for idx in range(1, len(arr[1])):
    link.append(arr[1][idx])

pre = 0

while len(link) != pre:
    pre = len(link)

    for num in link:
        for idx in range(1, len(arr[num])):
            if arr[num][idx] not in link:
                link.append(arr[num][idx])

print(pre - 1)