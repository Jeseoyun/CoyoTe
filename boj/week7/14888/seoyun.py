_MAX = -10**9
_MIN = 10**9


def calculate(idx, curr, nums, opers):
    global _MIN, _MAX
    if idx == len(nums)-1:
        _MIN = min(curr, _MIN)
        _MAX = max(curr, _MAX)
        return

    if opers[0]:
        opers[0] -= 1
        calculate(idx+1, curr+nums[idx+1], nums, opers)
        opers[0] += 1

    if opers[1]:
        opers[1] -= 1
        calculate(idx+1, curr-nums[idx+1], nums, opers)
        opers[1] += 1

    if opers[2]:
        opers[2] -= 1
        calculate(idx+1, curr*nums[idx+1], nums, opers)
        opers[2] += 1

    if opers[3]:
        opers[3] -= 1
        calculate(idx+1, int(curr/nums[idx+1]), nums, opers)
        opers[3] += 1


def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    operations = list(map(int, input().split()))

    calculate(0, numbers[0], numbers, operations)

    print(_MAX, _MIN, sep="\n")


if __name__ == "__main__":
    main()