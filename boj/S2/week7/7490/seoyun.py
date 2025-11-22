def calculate(expr):
    nums = []
    opers = []

    pre = ''
    for e in expr:
        if e in ('+', '-'):
            opers.append(e)
            nums.append(pre)
            pre = ''
        elif e == ' ':
            continue
        else:
            pre += e

    nums.append(pre)
    nums = list(map(int, nums))

    calculated = nums[0]
    for i in range(len(opers)):
        if opers[i] == "+":
            calculated += nums[i+1]
        if opers[i] == "-":
            calculated -= nums[i+1]

    return calculated


def dfs(i, N, curr, result):
    # print(curr)
    if i == N:
        val = calculate(curr)
        if val == 0:
            result.append(curr)
        return

    # 공백 넣기
    dfs(i+1, N, curr+f" {i+1}", result)

    # 더하기 넣기
    dfs(i+1, N, curr+f"+{i+1}", result)

    # 빼기 넣기
    dfs(i+1, N, curr+f"-{i+1}", result)



def main():
    T = int(input())

    for tc in range(T):
        if tc != 0:
            print()

        N = int(input())

        result = []
        dfs(1, N, '1', result)

        print(*result, sep='\n')


if __name__ == "__main__":
    main()
    # calculate("1+2-3+4-5-6+7")