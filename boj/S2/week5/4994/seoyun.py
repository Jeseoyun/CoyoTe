from collections import deque


def find_one_zero_num(target):
    queue = deque(['1'])
    visited = set()
    visited.add('1')

    while queue:
        curr_num = queue.popleft()

        for n in ('0', '1'):
            next_num = curr_num + n

            if next_num in visited:
                continue

            if int(next_num) % int(target) == 0:
                return next_num

            if len(next_num) > 100:
                return -1

            queue.append(next_num)
            visited.add(next_num)


def main():
    while True:
        n = input()

        if n == '0':
            break

        print(find_one_zero_num(n))


if __name__ == "__main__":
    main()