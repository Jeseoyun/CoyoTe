from collections import deque

def main():
    num = int(input())
    asc_queue = deque(list(range(1, num + 1)))
    goal_queue = deque()
    stack = deque()
    result_arr = []

    for _ in range(num):
        goal_queue.append(int(input()))

    is_no = False
    while asc_queue or stack:
        # print(result_arr)
        # 스택 비어있으면
        if not stack:
            top_num = asc_queue.popleft()
            stack.append(top_num)
            result_arr.append('+')
            continue

        # 탈출 로직
        if not asc_queue and stack[-1] > goal_queue[0]:
            is_no = True
            break

        # 뺴는 로직
        if goal_queue[0] == stack[-1]:
            goal_queue.popleft()
            stack.pop()
            result_arr.append('-')
            continue

        # 추가하는 로직
        if goal_queue[0] != stack[-1]:
            # print(goal_queue[0], stack[-1])
            top_num = asc_queue.popleft()
            stack.append(top_num)
            result_arr.append('+')
            continue
        

    #no 거나 stack이 남은 경우
    if is_no or stack:
        print("NO")
    else:
        for i in result_arr:
            print(i)



if __name__ == "__main__":
    main()