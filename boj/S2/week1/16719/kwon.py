# https://www.acmicpc.net/problem/16719
# ZOAC

import sys

sys.setrecursionlimit(10**6)

string = sys.stdin.readline().strip()
length = len(string)

visited = [False] * length

def select_char(start, end):
    """
    주어진 범위(start ~ end)에서 가장 작은 문자를 찾아 출력하고,
    그 문자의 오른쪽과 왼쪽 부분에 대해 재귀적으로 함수를 호출합니다.
    """

    if start > end:
        return

    min_char = 'Z' + '1' 
    min_idx = -1
    for i in range(start, end + 1):
        if string[i] < min_char:
            min_char = string[i]
            min_idx = i

    visited[min_idx] = True


    current_result = ""
    for i in range(length):
        if visited[i]:
            current_result += string[i]
    print(current_result)
    select_char(min_idx + 1, end)
    select_char(start, min_idx - 1)


# char_list = list(input())
# length = len(char_list)

# result = char_list[0]
# min_i = 0
# for i, c in enumerate(char_list):
#     if c < result:
#         min_i = i
#         result = c

# left = min_i - 1
# right = min_i + 1

# print(result)

# while left >= 0 or right < length:
#     cur_char = "Z" * 100

#     is_left = False
#     if left >= 0:
#         cur_char = char_list[left] + result
#         left -= 1
#         is_left = True
    
#     if right < length and result + char_list[right] < cur_char:
#         cur_char = result + char_list[right]
#         right += 1
#         if is_left:
#             left += 1
#             is_left = False
    
#     result = cur_char
#     print(result)
select_char(0, length - 1)