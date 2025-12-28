# 백준: 해밍 경로
# 이진 코드에서 하나씩만 다른 코드들을 계속 나열하는 것이 해밍 경로
from collections import deque

import sys
inputf = sys.stdin.readline

def BFS():
    pass

def main():
    num, str_length = map(int, inputf().split())

    # 경로 탐색 문제임
    # 시작점은 1번 코드, 끝나는 지점은 n번 코드
    # 결국 최단 경로를 구하는 문제다.
    # 그럼 들어오는 input들을 그래프로 만들어야 함.
    # 그래프로 어떻게 만들지?
    # 노드는 쉽다. str으로 저장해도 되고 이진수를 아예 정수로 바꿔도 됨
    # edge는? 100000개의 노드를 하나씩 비교하면 n^2번 인접 여부를 판단해야 함. 너무 많이 걸림

    # 그래프를 꼭 만들어야 하는가? BFS는 한번 훑는 로직임.
    # 쭉 한번 훑으면서 
    codes = []
    code2order = {}
    order2code = {}
    for i in range(num):
        input_code = int(inputf(), 2)# 2진수로 인식
        codes.append(input_code)
        code2order[i+1] = input_code
        order2code[input_code] = i + 1
    
    # print(codes)
    start_code = codes[0]
    codes = set(codes)

    queue = deque([start_code])
    visited = {start_code: start_code} #방문처리 겸 이전 노드 저장. 거꾸로 되짚을 수 있게
    parent_node = start_code
    
    # 덧셈 뺄셈으로 비트 연산을 하려고 했음.
    # while queue:
    #     cur_node = queue.popleft()
    #     parent_node = cur_node

    #     # 1, 2, 4, ... n 자리 만큼 더하기 빼기
    #     for i in range(str_length):
    #         some = 2 ** i

    #         for j in range(2):
    #             next_node = cur_node + ((-1) ** j) * some

    #             if next_node < 0:
    #                 continue
    #             if next_node in visited:
    #                 continue
    #             if not (next_node in codes):
    #                 continue
                
    #             visited[next_node] = parent_node
    #             queue.append(next_node)
    #             # print(visited)
    while queue:
        cur_node = queue.popleft()

        # 0번째부터 str_length-1번째 비트까지 하나씩 뒤집음
        for i in range(str_length):
            # 1 << i 는 i번째 비트만 1이고 나머지는 0인 수 (1, 2, 4, 8...)
            next_node = cur_node ^ (1 << i)

            if next_node in visited or next_node not in codes:
                continue
            
            # 방문 처리: key는 다음 노드 값, value는 현재 노드 값 (역추적용)
            visited[next_node] = cur_node
            queue.append(next_node)

    # 결과를 출력
    print_cnt = int(inputf())

    # print("방문처리")
    # print(visited)

    for _ in range(print_cnt):
        goal = int(inputf())
        goal_num = code2order[goal]

        # append 하고 나중에 pop하면서 출력
        cur_num = goal_num
        stack = []
        # 없거나 끝에 도달하면 됨
        while cur_num in visited:
            if cur_num == start_code:
                stack.append(order2code[cur_num])
                break
            # stack을 넣을때도 반대로 해줘야 함.
            stack.append(order2code[cur_num])
            cur_num = visited[cur_num]

        # goal에 맞는 출력 준비(경로 역추적 구현)
        # print(stack)

        # -1 출력 여부
        if stack and stack[-1] == 1:
            for node in reversed(stack):
                print(node, end=" ")
        else:
            print(-1)
        print()

if __name__ == "__main__":
    main()