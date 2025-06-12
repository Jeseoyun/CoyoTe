def main():
    test_num = int(input())

    # 그냥 nCm 하면 되는거 아님?
    for _ in range(test_num):
        left_num, right_num = map(int, input().split())
        
        result = 1
        div_num = 1

        for i in range(left_num):
            result = result * (right_num - i)
            div_num = div_num * (i+1)

        result = result / div_num
        print(int(result))

if __name__ == "__main__":
    main()