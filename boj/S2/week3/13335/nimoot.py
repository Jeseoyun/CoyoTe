n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w

bridge[0] = truck[0]
del truck[0]
ans = 1

while len(truck) > 0:
    if sum(bridge) - bridge[-1] + truck[0] <= l:
        bridge = [truck[0]] + bridge[:-1]
        del truck[0]
    else:
        bridge = [0] + bridge[:-1]
    ans += 1
    
last_truck = -1
for i in range(w):
    if bridge[i] != 0:
        last_truck = i
        break
ans += (w-last_truck)


print(ans)