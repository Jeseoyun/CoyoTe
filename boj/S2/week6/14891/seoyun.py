from collections import deque


TOTAL_GEAR = 4


def calculate_score(gears):
    total_score = 0
    for i in range(TOTAL_GEAR):
        if gears[i][0] == '1':
            total_score += 2**i

    return total_score


def main():
    gears = [deque(list(input())) for _ in range(TOTAL_GEAR)]
    K = int(input())

    for _ in range(K):
        gear_num, spin_cnt = map(int, input().split())
        gn = gear_num - 1

        queue = deque([gn])
        spin = [0]*TOTAL_GEAR
        spin[gn] = spin_cnt

        while queue:
            curr = queue.popleft()
            left = curr-1
            right = curr+1

            if (left >= 0) and spin[left] == 0 and (gears[curr][6] != gears[left][2]):
                # gears[left].rotate(-spin_dir)
                spin[left] = -spin[curr]
                queue.append(left)

            if (right < TOTAL_GEAR) and spin[right] == 0 and (gears[curr][2] != gears[right][6]):
                # gears[right].rotate(-spin_dir)
                spin[right] = -spin[curr]
                queue.append(right)

            # gears[curr].rotate(spin_cnt)

        for i in range(TOTAL_GEAR):
            if spin[i]:
                gears[i].rotate(spin[i])

    print(calculate_score(gears))


if __name__ == "__main__":
    main()
