# 백준: 01 타일

import sys
inputf = sys.stdin.readline

def main():
    num = int(inputf())

    # 1, 2, 3, 5, 8 ...
   
    if num == 1:
        print(1)
        return
    if num == 2:
        print(2)
        return

    prev2 = 1
    prev1 = 2
    
    for _ in range(3, num + 1):
        cur = (prev2 + prev1) % 15746

        prev2 = prev1
        # 나머지 연산
        # (a + b) % c == ((a % c) + (b % c)) % c
        prev1 = cur
    
    print(prev1)


if __name__ == "__main__":
    main()