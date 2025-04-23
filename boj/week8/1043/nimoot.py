# n: 사람 수, m: 파티 수
n, m = map(int, input().split())

# 진실을 아는 사람들의 정보 (첫 번째 값은 진실을 아는 사람 수)
truth = list(map(int, input().split()))

party = []

# 각 파티에 참여하는 사람들의 명단을 입력받아 저장 (맨 앞 숫자는 사람 수이므로 제외)
for _ in range(m):
    party.append(list(map(int, input().split()))[1:])  # 사람 수 제외하고 명단만 저장

# 만약 진실을 아는 사람이 없다면, 모든 파티에서 거짓말 가능
if truth[0] == 0:
    print(m)
else:
    # 진실을 아는 사람들의 집합 (처음엔 truth 리스트에서 첫 번째 수 제외)
    truthset = set(truth[1:])
    prelen = len(truthset)  # 이전 집합 크기 (진실 전파가 멈췄는지 체크용)

    while True:
        # 모든 파티를 순회하면서 진실을 알고 있는 사람이 있는지 체크
        for nums in party:
            isin = False  # 파티에 진실을 아는 사람이 있는지 여부
            for num in nums:
                if num in truthset:
                    isin = True
                    break  # 하나라도 있으면 진실 퍼짐
            if isin:
                # 그 파티의 모든 사람도 진실을 알게 됨
                for num in nums:
                    truthset.add(num)

        # 더 이상 진실이 퍼지지 않으면 루프 종료
        if prelen == len(truthset):
            ans = m  # 일단 모든 파티에서 거짓말 가능하다고 가정
            for nums in party:
                ithas = False  # 현재 파티에 진실 아는 사람 있는지
                for num in nums:
                    if num in truthset:
                        ithas = True
                        break
                if ithas:
                    ans -= 1  # 진실을 아는 사람이 있으면 거짓말 못 하니까 제외
            print(ans)
            exit()
        else:
            # 진실이 더 퍼졌으면 계속 반복
            prelen = len(truthset)
