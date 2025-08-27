from collections import deque


def main():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())  # 문서 수, 타겟 문서
        priority = list(map(int, input().split()))  # 문서의 중요도

        # 1. 가장 앞의 문서의 중요도 확인
        # 2. 나머지 문서들 중 중요도 높은게 하나라도 있으면 현재 문서를 큐의 가장 뒤에 삽입, 그렇지 않으면 바로 인쇄
        pq = deque(priority)

        idx_order = [i for i in range(N)]
        out = []
        while pq:
            curr = pq.popleft()
            idx = idx_order[0]
            if any(docs > curr for docs in pq):
                pq.append(curr)
                idx_order = idx_order[1:] + [idx_order[0]]
            else:
                out.append(idx)
                idx_order = idx_order[1:]

        print(out.index(M)+1)


if __name__ == "__main__":
    main()