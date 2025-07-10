MAX_NUM = float('inf')

def main():
    num = int(input())
    total = 0
    arange_arr = []

    for _ in range(num):
        jewel_num = int(input())
        score = 0
        jewel = list(map(int, input().split()))
        dp_list = [[-MAX_NUM, 0] for _ in range(jewel_num)]

        # print(jewel)
        # print(dp_list)

        for idx in range(jewel_num):
            if idx == 0:
                dp_list[idx][0] = jewel[idx]
                dp_list[idx][1] = 1
                continue
            
            if dp_list[idx-1][0]+jewel[idx] > jewel[idx]:
                dp_list[idx][0] = dp_list[idx-1][0]+jewel[idx] 
                dp_list[idx][1] = dp_list[idx-1][1]+1 
            elif dp_list[idx-1][0]+jewel[idx] == jewel[idx]:
                dp_list[idx][0] = jewel[idx]
                dp_list[idx][1] = 1
            else:
                dp_list[idx][0] = jewel[idx]
                dp_list[idx][1] = 1
            
        score_arr = max(dp_list, key=lambda x: (x[0], -x[1]))
        score = score_arr[0]

        start_idx = dp_list.index(score_arr)
        arange_arr.append([start_idx+2 - score_arr[1], start_idx+1])

        # print(score)

        total += score
    print(total)
    for arr in arange_arr:
        print(arr[0], end=" ")
        print(arr[1])

if __name__ == "__main__":
    main()