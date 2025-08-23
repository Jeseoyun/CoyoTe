import sys

total = int(sys.stdin.readline().strip())
ziphap = set()

for _ in range(total):
    cal = sys.stdin.readline().strip().split()
    
    if cal[0] == "add":
        ziphap.add(int(cal[1]))
    elif cal[0] == "remove":
        ziphap.discard(int(cal[1]))
    elif cal[0] == "check":
        print(1 if int(cal[1]) in ziphap else 0)
    elif cal[0] == "toggle":
        num = int(cal[1])
        if num in ziphap:
            ziphap.discard(num)
        else:
            ziphap.add(num)
    elif cal[0] == "all":
        ziphap = {i for i in range(1, 21)}
    elif cal[0] == "empty":
        ziphap.clear()
