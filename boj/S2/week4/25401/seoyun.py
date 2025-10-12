from collections import defaultdict


def main():
    N = int(input())
    cards = list(map(int, input().split()))

    max_fixed_card = 1

    for i in range(N):
        diff_count = defaultdict(int)

        for j in range(i+1, N):
            diff = cards[j]-cards[i]
            gap = j-i

            if diff % gap == 0:
                change = diff // gap
                diff_count[change] += 1

                if diff_count[change] + 1 > max_fixed_card:
                    max_fixed_card = diff_count[change] + 1

    print(N - max_fixed_card)


if __name__ == "__main__":
    main()