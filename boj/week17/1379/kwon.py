import heapq

N = int(input())

lessons = []
for _ in range(N):
    i, s, e = map(int, input().split())
    lessons.append((s, e, i - 1))

lessons.sort()
room_end = [(lessons[0][1], 1)]
result = [0] * N
result[lessons[0][-1]] = 1
room_cnt = 1

for s, e, i in lessons[1:]:
    # 가장 일찍 끝나는 방
    min_end, room_i = heapq.heappop(room_end)
    # print("room_end:", room_end)
    # 그 방을 사용 가능할 경우
    if min_end <= s:
        # print(e, room_i)
        heapq.heappush(room_end, (e, room_i))
        result[i] = room_i
    # 사용 못하는 경우 -> 새로운 방
    else:
        # 원래대로 복구
        heapq.heappush(room_end, (min_end, room_i))
        # 새로운 방 만들기
        room_cnt += 1
        result[i] = room_cnt
        heapq.heappush(room_end, (e, room_cnt))

print(room_cnt)
print(*result, sep='\n')