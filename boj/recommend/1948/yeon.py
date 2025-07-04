# 임계경로 
# https://www.acmicpc.net/problem/1948


# 일방통행에 싸이클이 없다. -> Directed Acyclic Graph (DAG)

import sys 
from collections import defaultdict, deque 

inputf = sys.stdin.readline

def main():

    n = int(inputf())  # 도시의 개수 
    m = int(inputf())  # 도로의 개수 

    graph= defaultdict(list)  # k:v = src:(dst, cost)
    reversed_graph = defaultdict(list)  # k:v = dst:(src, cost)

    for _ in range(m):
        src, dst, cost = map(int, inputf().rstrip().split())  # 출발 도시, 도착 도시, 도로 비용(시간)
        graph[src].append((dst, cost))  
        reversed_graph[dst].append((src, cost))  # 역방향 그래프도 저장

    SRC, DST = map(int, inputf().rstrip().split())  # 지도를 그리는 사람들이 출발하는 도시(SRC)와 도착하는 도시(DST)

    # from SRC to DST 인 모든 경로에 대해서 cost(시간)가 가장 오래 걸리는 경로를 구해야 한다.

    # 1. 위상 정렬을 통해서 SRC에서 각 노드까지의 최장 경로를 구한다.
    max_time_from_src = [0 for _ in range(n + 1)]  # 각 노드까지의 최장 경로 길이 (소요 시간)
    # number_of_roads = [0] * (n + 1)  # 각 노드까지의 최장 경로에 포함된 도로의 개수
    indegree = [0] * (n + 1)  # 진입 차수

    for i in range(1, n+1):
        indegree[i] = len(reversed_graph[i])

    queue = deque([SRC])  # 위상 정렬을 위한 큐
    while queue:
        node = queue.popleft()

        for neighbor, cost in graph[node]:
            indegree[neighbor] -= 1
            max_time_from_src[neighbor] = max(max_time_from_src[neighbor], max_time_from_src[node] + cost)
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # print(max_time_from_src[DST])  # debugging: SRC에서 DST까지의 최장 경로 길이 (소요 시간)

    # 최장 경로 내에 포함되는 도로를 구한다. 
    # DST 로 부터 시작하는 역방향 위상 정렬을 통해서 최장 경로에 포함되는 도로를 구한다. 
    # 최장 경로 포함 도로 조건 
    # src - u - v - dst 일 때 (v가 dst일 수 있음). -> 아래 while 문에서 첫 번재 queue.popleft() 하는 node가 v이자 dst가 된다.
    # max_time_from_src[u] + cost(u,v) + max_time_to_dst[v] == max_time_from_src[DST]
    # 여기서 max_time_to_dst[v] 는 v에서 DST 까지의 최장 경로 소요 시간.
    #  

    count_roads = set()  # 최장 경로에 포함되는 도로 집합: (src, dst) 형태로 저장
    max_time_to_dst = [0 for _ in range(n+1)]  # 각 노드에서 DST 까지의 최장 경로 길이 (소요 시간))
    queue = deque([DST])  # 역방향 위상 정렬을 위한 큐 
    while queue:
        node = queue.popleft()
        for neighbor, cost in reversed_graph[node]:
            if max_time_from_src[neighbor] + cost + max_time_to_dst[node] == max_time_from_src[DST]:  # 최장 경로 조건을 만족하는 경우
                count_roads.add((neighbor, node))  # (src, dst) 형태로 최장 경로 포함 도로에 추가 
                max_time_to_dst[neighbor] = max(max_time_to_dst[neighbor], max_time_to_dst[node] + cost)  # DST 까지의 최장 경로 길이 갱신
                if neighbor not in queue:  # 큐에 없으면 추가
                    queue.append(neighbor)

    
    print(max_time_from_src[DST])  # SRC에서 DST까지의 최장 경로 길이 (소요 시간)
    print(len(count_roads))  # 최장 경로에 포함되는 도로의 개수
    

    return

if __name__=='__main__':
    main()