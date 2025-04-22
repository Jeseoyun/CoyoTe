from collections import deque


MAX = 100000


def get_shortest_time(start, end):
    queue = deque()
    visited = [False] * (MAX + 1)
    queue.append((start, 0))
    visited[start] = True

    while queue:
        curr_pos, cost = queue.popleft()
        # print(curr_pos, cost)
        if curr_pos == end:
            return cost

        for next_pos in (curr_pos*2, curr_pos-1, curr_pos+1):
            if next_pos < 0 or next_pos > MAX:
                continue
            if visited[next_pos]:
                continue

            if next_pos == curr_pos*2:
                queue.appendleft((next_pos, cost))
            else:
                queue.append((next_pos, cost+1))
            visited[next_pos] = True


def main():
    N, K = map(int, input().split())
    result = get_shortest_time(N, K)
    print(result)


if __name__ == "__main__":
    main()