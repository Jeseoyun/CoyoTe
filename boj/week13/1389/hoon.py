# 문제 그림좀 그려줘라

INF = float('inf')

def main():
    friend_num, rel_num = map(int, input().split())
    # 양방향 그래프
    graph = [[INF] * friend_num for _ in range(friend_num)]

    for _ in range(rel_num):
        first, second = map(int, input().split())
        graph[first-1][second-1] = 1
        graph[second-1][first-1] = 1

    for mid in range(friend_num):
        for first in range(friend_num):
            for second in range(friend_num):
                if first == second:
                    continue
                if graph[first][second] > graph[first][mid] + graph[mid][second]:
                    graph[first][second] = graph[first][mid] + graph[mid][second]
                    graph[second][first] = graph[first][second]
    
    min_num = INF
    min_people = -1

    for y in range(friend_num):
        score = 0
        for x in range(friend_num):
            if y == x:
                continue
            score = score + graph[y][x]
        if min_num > score:
            min_people = y+1
            min_num = score        

    # 디버깅
    # print()
    # for y in range(friend_num):
    #     for x in range(friend_num):
    #         print(graph[y][x], end=" ")
    #     print()
    # print()

    print(min_people)


if __name__ == "__main__":
    main()