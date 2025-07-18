import heapq
from collections import defaultdict


def main():
    n = int(input())
    lecture_info = [list(map(int, input().split())) for _ in range(n)]
    lecture_info = sorted(lecture_info, key=lambda x: (x[1], x[2]))

    remain_lecture = []

    # for no, start, end in lecture_info:
    #     print(f"{no, start, end}")

    assigned = 0
    room = defaultdict(int)  # {lecture_no: room_no}

    for no, start, end in lecture_info:
        if remain_lecture and remain_lecture[0][0] <= start:
            finish_time, room_num = heapq.heappop(remain_lecture)
        else:
            assigned += 1
            room_num = assigned

        heapq.heappush(remain_lecture, (end, room_num))
        room[no] = room_num


    print(assigned)
    for i in range(1, n+1):
        print(room[i])


if __name__ == "__main__":
    main()