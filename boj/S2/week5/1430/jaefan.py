# 공격
# https://www.acmicpc.net/problem/1430

from collections import defaultdict, deque

def get_distance(source, destination):
    return ((source[0] - destination[0]) ** 2 + (source[1] - destination[1]) ** 2) ** 0.5


def bfs_max_energy(graph, start, attackable_towers, D, N):
    """start 탑에서 출발해서 공격 가능한 탑 중 최대 에너지를 전달할 수 있는 값 반환"""
    visited = [-1] * N  # 거리 저장 (-1은 미방문)
    queue = deque([start])
    visited[start] = 0
    
    max_energy = 0.0
    
    while queue:
        current = queue.popleft()
        current_dist = visited[current]
        
        # 현재 탑이 공격 가능한 탑이면 에너지 계산
        if current in attackable_towers:
            energy = D * (0.5 ** current_dist)  # 공격가능한 탑 까지의 거리에 따라 에너지를 분배 (거리의 제곱, 여기서 거리는 중간에 있는 타워의 개수)
            max_energy = max(max_energy, energy)  # 최대 에너지 갱신 
        
        # 인접 탑 탐색
        for next_tower in graph[current]:
            if visited[next_tower] == -1:
                visited[next_tower] = current_dist + 1
                queue.append(next_tower)
    
    return max_energy


def main():
    N, R, D, X, Y = map(int, input().split())  # N: 탑의 개수, R: 탑의 사정거리, D, 초기 에너지, X: 적의 X좌표, Y: 적의 Y좌표

    towers = dict()
    for i in range(N):
        x, y = map(int, input().split())
        towers[i] = (x, y)

    # 서로 다른 두 탑의 거리가 R 보다 작다면, 탑의 에너지를 분배할 수 있다. 에너지를 분배하는 경우에 분배하는 
    # 에너지는 1/2 가 된다.
    # 적이 받는 최대 데미지를 계산한다.
    
    # 그래프 모델링 
    # 타워 간 거리가 R 이하인 타워들을 간선으로 연결한다. 
    # TODO: graph modeling 
    graph = defaultdict(list)
    for i in range(N):
        for j in range(i+1, N):
            if get_distance(towers[i], towers[j]) <= R:
                graph[i].append(j)
                graph[j].append(i)


    # 현재 적을 공격 가능한 탑을 찾는다. 
    attackable_towers = []
    for i in range(N):
        if get_distance(towers[i], (X, Y)) <= R:
            attackable_towers.append(i)
    
    # print(f"디버그 - 탑 좌표: {towers}")
    # print(f"디버그 - 적 좌표: ({X}, {Y})")
    # print(f"디버그 - 공격 가능한 탑: {attackable_towers}")
    # print(f"디버그 - 그래프: {dict(graph)}")

    # 공격 가능한 탑을 모두 찾았다면, 어떻게 에너지를 재분배하는 것이 가장 큰 에너지로 공격을 할 수 있는지 게산한다. 
    total_energy = 0.0
    # 모든 탑에서 BFS 수행 - 각 탑의 에너지는 가장 가까운 공격 가능한 탑으로 전달한다. 
    for i in range(N):
        max_energy = bfs_max_energy(graph=graph, start=i, attackable_towers=attackable_towers, D=D, N=N)
        # if max_energy > 0:
        #     print(f"디버그 - 탑 {i}에서 최대 에너지: {max_energy}")
        total_energy += max_energy

    # print(f"디버그 - 총 에너지: {total_energy}")


    # 최종 답
    print(total_energy)
    return 

if __name__ == "__main__":
    main()