def boy_rule(given, status):
    """ 스위치 번호가 given의 배수일 경우 스위치 상태 변경 """
    for i in range(1, len(status)//given+1):
        # print(i*given, "번째 변경", status[i*given], "->", status[i*given]^1)
        status[i*given-1] ^= 1

def girl_rule(given, status):
    """ 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간 """
    return


def main():
    N = int(input())  # 스위치 개수
    status = list(map(int, input().split()))  # 스위치 상태

    SN = int(input())  # 학생 수
    gender_rule_map = {
        1: boy_rule,
        2: girl_rule
    }

    for _ in range(SN):
        gender, given = map(int, input().split())
        gender_rule_map[gender](given, status)

    print(" ".join(map(str, status)))


if __name__ == "__main__":
    main()