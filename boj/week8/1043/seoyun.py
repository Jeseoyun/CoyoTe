class DisjointSet:
    def __init__(self, N):
        self.N = N
        self.p = [i for i in range(N+1)]
        self.rank = [0] * (N+1)

    def find_set(self, x):
        ''' 루트 노드 찾기 '''
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, a, b):
        ''' 두 개의 원소를 합집합으로 만들기 '''
        pa = self.find_set(a)
        pb = self.find_set(b)

        if pa != pb:
            if self.rank[pa] > self.rank[pb]:
                self.p[pb] = pa
            elif self.rank[pa] < self.rank[pb]:
                self.p[pa] = pb
            else:
                self.p[pb] = pa
                self.rank[pa] += 1


def main():
    N, M = map(int, input().split())  # 사람 수, 파티 수
    tk_n, *truth_known = map(int, input().split())
    truth_known = set(truth_known)

    parties = []
    for party_num in range(M):
        p_n, *participant = map(int, input().split())
        parties.append(participant)

    # 진실을 아는 그룹을 찾기 위해 disjoint set 만들기
    ds = DisjointSet(N)
    for party in parties:
        first = party[0]
        for person in party[1:]:
            ds.union(first, person)

    lie_party = 0
    truth_roots = set(ds.find_set(x) for x in truth_known)
    for party in parties:
        if any(ds.find_set(person) in truth_roots for person in party):
            continue
        else:
            lie_party += 1

    print(lie_party)


if __name__ == "__main__":
    main()