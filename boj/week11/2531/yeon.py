# 회전 초밥
# https://www.acmicpc.net/problem/2531

def main():

    N, d, k ,c = map(int, input().split())  # N: 접시 수, d: 초밥 종류 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
    sushi = [int(input()) for _ in range(N)]

    sushi += sushi[:k-1] # 원형으로 만들기 위해서

    # print(sushi)  # debug

    max_sushi = 0  # 최대 초밥 종류 수
    # 연속으로 k 개 먹을 수 있는 경우의 수 
    for i in range(len(sushi)-k+1):
        # 연속으로 k 개 먹을 수 있는 경우의 수
        eat = sushi[i:i+k]
        # print(eat)  # debug

        # 현재 쿠폰 번호가 포함되어 있지 않으면 추가 
        if c not in eat:
            eat.append(c)
        # 초밥 종류 수
        eat = set(eat)
        # print(eat)  # debug
        # 최대 초밥 종류 수
        max_sushi = max(max_sushi, len(eat))
    print(max_sushi)

if __name__=='__main__':
    main()