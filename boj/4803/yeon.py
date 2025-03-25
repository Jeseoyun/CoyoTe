# 트리 
# https://www.acmicpc.net/problem/4803


from collections import defaultdict, deque

def is_tree(graph:dict, component:set):
    """트리 판별 함수 (사이클 판별)
    """

    # 트리 조건
    # 1. n 개의 정점과 n-1 개의 간선
    # 2. 사이클이 없어야 한다. 
    # 3. 임의의 두 정점에 대해서 유일한 경로를 가진다. 
    # 4. 2번과 3번은 동일한 맥락이다? 
    
    # 접근 방식: 사이클이 존재한다. -> 정점 v 를 시작으로 탐색 -> 인접 노드 중 직전 노드가 아닌데, 방문이 되어 있다. -> 사이클 
    # BFS를 현재 노드 이외에 직전 노드도 관리를 해주어야 할 것 같다. (탐색 큐)

    if len(component) == 1:
        return True  # 정점 하나짜리는 사이클 없으므로 트리

    visited = set()
    dq = deque()
    
    # 임의의 시작점 하나에서만 탐색
    start = list(component)[0]
    dq.append((start, 0))  # (현재노드, 직전노드): 직전 노드는 임의 지정 (0번 정점은 없는 그래프 상 없는 정점)

    while dq:
        curr, prev = dq.popleft()
        if curr in visited:  # 현재 노드 방문한 경우 스킵 
            continue
        visited.add(curr)  # 현재 노드 방문 처리 

        for adj in graph[curr]:  # 인접 노드 순회 
            if adj == prev:  # 직전 노드인 경우 스킵 
                continue
            if adj in visited:  # 직전 노드가 아닌데, 방문한 경우 -> 사이클
                return False  # 사이클 발생
            
            dq.append((adj, curr))  # 사이클이 아닌 노드의 경우 탐색 큐에 추가 

    # 모든 정점을 방문했는지 확인 (연결되어 있어야 함)
    return visited == component


def print_result(tc, num_trees):
    """ 결과 출력 함수 
    """
    if num_trees > 1:
        return f"Case {tc}: A forest of {num_trees} trees."
    elif num_trees == 1:
        return f"Case {tc}: There is one tree."
    else:
        return f"Case {tc}: No trees."


def get_connected_components(n:int, graph:dict) -> list:
    connected_components = list()

    # 1번 정점부터 모든 정점을 방문할 때까지 반복 
    # 1번 정점을 시작으로 연결된 정점을 모두 하나의 connected component 로 여긴다. 
    # 더 이상 연결된 정점이 없는 경우 connected component로 정의한다. 
    
    visited = set()  # 방문 여부 집합 
    for i in range(1, n+1):  # 모든 정점 순회 
        if i in visited: continue   # 방문한 경우 지나친다.
        
        visited.add(i)  # 현재 정점 방문 처리 
        
        component = set()  # 현재 정점 i를 포함하는 connected component (정점들의 집합)
        
        dq = deque([i])  # BFS 할 deque 

        while dq:  # BFS (아래는 그냥 BFS)
            vertex = dq.popleft()
            if graph[vertex]: 
                component.add(vertex)
                for adj_vertex in graph[vertex]:
                    if adj_vertex in visited: continue 
                    component.add(adj_vertex)
                    visited.add(adj_vertex)
                    dq.append(adj_vertex)
            else:
                component.add(vertex)

        connected_components.append(component)  # 하나의 connected component 리스트 추가 
    
    # print(connected_components)


    return connected_components


def main():

    # 문제 입력 
    tc = 0
    while True:
        tc += 1
        n, m = map(int, input().split())
        if n == 0 and m == 0: break 

        graph = defaultdict(list)
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        # 접근 방법 
        # 1. connected component 들을 구한다.
        # 2. connected component가 tree 인지 확인한다. 
        # 3. tree인 경우 num_tree + 1 한다. 

        num_trees = 0

        if n == 0:
            print(print_result(tc=tc, num_trees=0))
            return 
        
        elif n == 1:
            print(print_result(tc=tc, num_trees=1))
            return 
        else:
            # 1. connected component 를 구한다. -> bfs 
            connected_components = get_connected_components(n=n, graph=graph)

            # 2. 각각의 connected components가 tree 인지 확인한다.
            for connected_component in connected_components:
                if is_tree(graph=graph, component=connected_component):
                    # 3. tree 인 경우 num_tree += 1
                    num_trees += 1

        print(print_result(tc=tc, num_trees=num_trees))
    return

if __name__=='__main__':
    main()