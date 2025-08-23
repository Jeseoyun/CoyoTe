# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

from itertools import permutations

def main():
    min_inf = float("inf")
    max_inf = float("-inf")

    N = int(input())

    nums = list(map(int, input().split()))
    opnum = list(map(int, input().split()))  # +, -, x, / 
    operators = list("+"*opnum[0] + "-"*opnum[1] + "*"*opnum[2] + "/"*opnum[3])
    ops_perm = list(permutations(operators))

    for ops in ops_perm:
        result = nums[0]
        for i in range(1, N):
            op = ops[i-1]
            if op == "+":
                result += nums[i]
                
            elif op == "-":
                result -= nums[i]

            elif op == "*":
                result *= nums[i]

            elif op == "/":
                # 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
                # 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
                # 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
                if result < 0 and nums[i] > 0:
                    result = -1*(((-1)*result) // nums[i])
                else:
                    result //= nums[i]
        
        if result < min_inf: 
            min_inf = result
        if result > max_inf:
            max_inf = result 

    print(max_inf)
    print(min_inf)
                                                                    
    return 

if __name__=='__main__':
    main()