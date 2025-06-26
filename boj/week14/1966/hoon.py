from collections import deque

def main():
    num = int(input())

    for _ in range(num):
        length, idx = map(int, input().split())

        data_list = list(map(int, input().split()))

        q = deque(data_list)

        cnt = 1
        
        while q:
            if q[0] < max(q):
                temp = q.popleft()
                q.append(temp)
            else:
                if idx == 0:
                    break
                    
                q.popleft()
                cnt = cnt + 1

            if idx > 0:
                idx = idx - 1
            else:
                idx = len(q) -1
        
        print(cnt)


if __name__ == "__main__":
    main()