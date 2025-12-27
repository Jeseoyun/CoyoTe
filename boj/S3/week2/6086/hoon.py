# 백준: 최대 유량
# 최소 용량은 BFS를 모든 노드에서 수행하면 되나? 26 * 700
# 최대 용량은 어떻게 해야됨??

# 어려운데???

# 너무 오래 고민한 끝에 답을 찾아보았고 에드몬드-카프 알고리즘이라는 걸 토대로 함.
# 이게 도대체 뭘까... 처음 보고, 봐도 이해가 너무 어려운데... 예전에 플래티넘이었던 문젠데 이거...
# 이건 풀었다고 하기도 그렇네

from collections import deque
import sys
inputf = sys.stdin.readline

def BFS(start, path, flow):
    queue = deque()
    queue.append(start)

    #해당 노드를 방문했는지 여부를 확인함과 동시에 어디에서 왔는지 '부모 노드'를 기록하는 용도임.
    visited = [-1] * 128
    visited[start] = start

    while queue:
        idx = queue.popleft()

        # 알파벳 아스키코드 돌기
        for i in range(65, 123):
            if visited[i] == -1 and path[idx][i] - flow[idx][i] > 0:
                queue.append(i)
                visited[i] = idx
    
    return visited

def merge_pipe(path):
    start, end = 65, 90 # A, Z 아스키코드
    flow = [[0] * 128 for _ in range(128)]
    result = 0

    while True:
        # A에서 Z로 가는 경로 찾기
        parent = BFS(start, path, flow)

        # 반복하다가 더 이상 z까지 도달할 경로가 없으면 탈출
        if parent[end] == -1:
            return result

        min_value = float('inf')

        idx = end
        while idx != start:
            # 현재 간선 용량 중 가장 작은 값을 선택함
            cur_parent = parent[idx]
            min_value = min(min_value, path[cur_parent][idx] - flow[cur_parent][idx])
            idx = cur_parent
        
        # 찾은 최소 유량을 경로 상의 간선에게 모두 업뎃하기
        idx = end
        while idx != start:
            cur_parent = parent[idx]
            # 순방향으로는 유량을 더하고
            flow[cur_parent][idx] += min_value

            # 역방향은 유량 빼
            flow[idx][cur_parent] -= min_value
            idx = cur_parent

        result += min_value

def main():
    num = int(inputf())
    
    # 각 간선의 최대 용량을 저장하는 인접 행렬
    path = [[0]*128 for _ in range(128)]

    for _ in range(num):
        start, end, num = inputf().split()

        #유니코드로 변경
        start_code = ord(start)
        end_code = ord(end)
        weight = int(num)

        # 양방향으로 만듬. 이게 핵심인데
        path[start_code][end_code] += weight
        path[end_code][start_code] += weight

    # 최대 유량 계산 및 출력
    print(merge_pipe(path))

if __name__ == "__main__":
    main()