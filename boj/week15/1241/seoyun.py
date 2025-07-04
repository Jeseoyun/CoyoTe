from collections import Counter


# def main():
#     N = int(input())
#     numbers = [int(input()) for _ in range(N)]
#
#     for curr_student in range(N):
#         toktok = 0
#         for interval in range(N-1):
#             compare_student = (curr_student + interval + 1) % N
#
#             if numbers[curr_student] % numbers[compare_student] == 0:
#                 toktok += 1
#
#         print(toktok)


def get_divisor(n):
    divisor = set()
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            divisor.add(i)
            if (i**2) != n:
                divisor.add(n//i)
    return divisor


def main():
    N = int(input().rstrip())
    numbers = [int(input().rstrip()) for _ in range(N)]

    # numbers[i]의 약수가 다른 놈들에 몇 개 있는지 찾아야 함
    # -> 연산 횟수를 최소한으로 줄이는 것이 중요

    # 1. 전체 수들의 등장 횟수를 미리 계산
    freq = Counter(numbers)

    # 2. 중복되는 약수 계산 줄이기 위해 약수 사전 만들어준다
    divisor_map = {n: get_divisor(n) for n in set(numbers)}

    # 3. 현재 숫자의 약수가 다른 놈들에 몇 개 있는지 찾기
    for i in range(N):
        toktok = 0
        curr = numbers[i]

        # 이 때, 현재 숫자의 약수에 대해서 입력받은 숫자의 개수만큼 더해준다.
        # 입력받은 수열보다 약수의 개수가 현저히 작을 경우 반복문을 덜 돌아 매우 효율적이게 된다.
        for d in divisor_map[curr]:
            toktok += freq[d]

        toktok -= 1  # 자기 자신은 무조건 약수로 가졌을 것이므로 1 빼준다
        print(toktok)


if __name__ == "__main__":
    main()