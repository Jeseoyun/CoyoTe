N = int(input())

P = list(map(int, input().split()))
S = list(map(int, input().split()))

def shuffle_card(cards, S):
    new_cards = [0] * (N)
    for i, n_i in enumerate(S):
        new_cards[n_i] = cards[i]
    return new_cards

cards = P[:]
answer = [0, 1, 2] * (N // 3)
cnt = 0

while answer != cards:
    cards = shuffle_card(cards, S)
    cnt += 1

    if cards == P:
        print(-1)
        break

else:
    print(cnt)