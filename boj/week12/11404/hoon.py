def main():
    city_num = int(input())
    bus_num = int(input())

    graph = [[987654321] * city_num for _ in range(city_num)]

    for _ in range(bus_num):
        info = input().split()
        start = int(info[0])
        end = int(info[1])
        cost = int(info[2])

        if graph[start-1][end-1] >= cost:
            graph[start-1][end-1] = cost
    
    # 디버깅
    # print()
    # for y in range(city_num):
    #     for x in range(city_num):
    #         print(graph[y][x], end=" ")
    #     print()

    # 알고리즘 사용
    for mid in range(city_num):
        for start in range(city_num):
            for end in range(city_num):
                #자기 자신 처리
                if start == end:
                    continue

                if graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
    
    for start in range(city_num):
        for end in range(city_num):
            if graph[start][end] >= 987654321:
                graph[start][end] = 0

    for y in range(city_num):
        for x in range(city_num):
            print(graph[y][x], end=" ")
        print()

if __name__ == "__main__":
    main()