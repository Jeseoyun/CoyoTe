MAX_SITE = 30
MEMO = [[-1]*MAX_SITE for _ in range(MAX_SITE)]


def comb(n, m):
    m = n-m if n//2 < m else m

    if m == 0 or n == m:
        return 1

    if MEMO[n][m] != -1:
        return MEMO[n][m]

    MEMO[n][m] = comb(n-1, m) + comb(n-1, m-1)

    return MEMO[n][m]


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        print(comb(M, N))


if __name__ == "__main__":
    main()