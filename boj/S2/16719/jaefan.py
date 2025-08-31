# ZOAC
# https://www.acmicpc.net/problem/16719

import sys 

inputf = sys.stdin.readline

def find_fastest_char(s:str, order: int, result:list):


    if len(s) == 0:  # 입력 문자열이 비어있으면 반환 
        return ""
    
    min_char = min(s)
    min_index = s.index(min_char)


    result[order + min_index] = min_char

    # print(f"order: {order}, s: {s}, min_char: {min_char}, min_index: {min_index}, result: {result}")

    print("".join(result))

    # 현재 가장 작은 문자를 기준으로 뒷 문자열 처리 (recursion)
    find_fastest_char(s[min_index+1:], order+min_index + 1, result)

    # 현재 가장 작은 문자열을 기준으로 앞 문자열 처리 (recursion)
    find_fastest_char(s[:min_index], order, result)


def main():
    S = inputf().strip()

    # TODO: 문자를 추가했을 때, 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여준다. 
    # 1. 문자열에 포함 된 문자 중 사전 순으로 가장 앞에 오는 문자를 선택한다. (첫 문자, 사전적 순서가 동일한 문자가 여러 개 있는 경우 index 가 빠른 문자를 선택한다.)
    # 2. 원본 문자열을 첫 문자를 기준으로 나눈다. (left, right)
    
    result = ["" for _ in range(len(S))]
    find_fastest_char(S, 0, result)

if __name__ == "__main__":
    main()