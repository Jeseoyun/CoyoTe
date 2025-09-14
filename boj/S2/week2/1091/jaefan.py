# 카드 섞기
# https://www.acmicpc.net/problem/1091

import sys

inputf = sys.stdin.readline

def shuffle(cards, S):
    N = len(cards)
    new_cards = [0] * N
    for i in range(N):
        new_cards[S[i]] = cards[i]
    return new_cards


def main():
    N = int(inputf())  # 카드의 수 
    P = list(map(int, inputf().split()))  # 목표 상태 
    S = list(map(int, inputf().split()))  # 섞는 방법
    
    # 초기 상태: 0, 1, 2, 0, 1, 2, ... 패턴
    cards = [i % 3 for i in range(N)]
    answer = P[:]

    # P[i] 는 i 번째 카드가 마지막에 가있어야 하는 플레이어 index를 의미한다. 
    # 위 조건을 만족하는 리스트를 만들기 어려우므로 cards와 answer 를 반대로 생각
    cards, answer = answer[:], cards[:]

    cnt = 0
    visited = set()

    # print(cards)
    # print(answer)
    
    # 목표 패턴이 될 때까지 섞기
    while cards != answer:
        # 현재 상태를 문자열로 변환하여 방문(이미 나온 애인지) 확인
        state = "".join(map(str, cards))
        if state in visited:
            print(-1)
            return
        visited.add(state)
        
        cards = shuffle(cards, S)
        cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    main()