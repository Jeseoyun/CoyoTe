from collections import deque

N, M = map(int, input().split())
truth_num, *truth_list = list(map(int, input().split()))

truth_set = set(truth_list)

party_graph = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

result_set = set()

def search_party():
    q =  truth_set.copy()
    visited = truth_set.copy()
    while q:
        cur = q.pop()
        # 들어있으면 q에 모두 넣어버리기
        for i, party in enumerate(party_graph):
            if cur in party:
                if i in result_set:
                    continue
                # print(party)
                result_set.add(i)
                # visited 제외
                q.update(party - visited)

search_party()

print(M - len(result_set))