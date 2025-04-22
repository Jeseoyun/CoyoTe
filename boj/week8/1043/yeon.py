# 거짓말 
"""
모든 파티에 참여해야 함 
거짓말쟁이가 되지 않으면서 과장된 이야기를 할 수 있는 파티의 최대 개수

- 진실을 아는 사람 수가 0이면 모든 파티에 참석할 수 있다.
- 진실을 아는 사람 수가 1명 이상이면 그 사람이 있는 파티에서는 거짓말 할 수 없다.
- 진실을 말한 파티에 참석한 사람은 진실을 아는 사람이 된다. 
- 진실을 아는 사람이 추가되는 경우 모든 파티에 대해서 다시 확인해야 한다. 
    -> 유니온 파인드? 제대로 구현할 수 있으려나 
"""

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x_root = find(parents, x)
    y_root = find(parents, y)
    if x_root != y_root:
        parents[y_root] = x_root


def main():

    N, M = map(int, input().split())  # 사람 수, 파티 수

    truth = list(map(int, input().split()))
    truth_set = set(truth[1:])  # 진실을 아는 사람 집합 
    parents = [i for i in range(N+1)]  # union-find를 위한 부모 노드 초기화
    parties = []

    # 각 파티에 참석한 사람들을 union-find로 묶어준다. 
    # -> 동일한 파티에 참석한 사람들끼리 같은 루트 설정 
    for _ in range(M):
        party = list(map(int, input().split()))
        parties.append(party[1:])  # party[0]은 파티에 참석한 사람 수
        for i in range(1, len(party)-1):
            union(parents, party[1], party[i+1])

    # 진실을 아는 사람 수가 0이면 모든 파티에 참석할 수 있다. 시간 최적화 ? 
    if len(truth) == 0:
        print(M)
        return
    
    # 진실을 아는 사람들의 경우 루트를 모두 동일하게 설정 
    truth_roots = [find(parents, mem) for mem in truth_set]
    
    max_parties = 0
    # 각 파티에 대해 진실을 아는 사람과 같은 루트를 가진 사람이 있는지 확인
    for party in parties:
        # party에 진실을 아는 사람이 있는지 확인
        if any(find(parents, mem) in truth_roots for mem in party):
            continue  # 진실을 아는 사람이 있는 경우 거짓말 할 수 없음
        max_parties += 1  # 진실을 아는 사람이 없는 경우 거짓말 할 수 있음

    print(max_parties)  # 거짓말 할 수 있는 파티의 최대 개수
    return

if __name__=='__main__':
    main()