# 집합
# https://www.acmicpc.net/problem/11723

import sys 

inputf = sys.stdin.readline  # 안쓰니까 타임오버
printf = sys.stdout.write  # print() -> 1628ms, printf() -> 2268ms : print() 압승 !!!1 
def main():

    M = int(inputf())
    tes = set()
    for _ in range(M):
        _input = inputf().split()
        cmd, x = _input[0], _input[-1]
        if x not in  {'all', 'empty'}:
            x = int(x)
        if cmd == "add":
            tes.add(int(x))
        elif cmd == "remove":
            if x in tes:
                tes.remove(int(x))
        elif cmd == "check":
            if x in tes:
                # printf(str(1) + "\n")  # 개행 안해주면 혼납니다.
                print(1)
            else: 
                # printf(str(0) + "\n")
                print(0)
        elif cmd == "toggle":
            if x in tes: 
                tes.remove(x)
            else: 
                tes.add(x)
        elif cmd == "all":
            tes = set(list(range(1, 21))) 
        else:
            tes.clear()

    return

if __name__=='__main__':
    main()