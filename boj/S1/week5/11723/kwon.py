import sys
input = sys.stdin.readline
print = sys.stdout.write

m = int(input())

s = set()

for _ in range(m):
    command = input().strip().split()

    if len(command) == 2:
        command, x = command
        command = command.strip()
        x = int(x)
    else:
        command = command[0]

    if command == 'add':
        s.add(x)
    elif command == 'remove':
        if x in s:
            s.remove(x)
    elif command == 'check':
        if x in s:
            print('1\n')
        else:
            print('0\n')
    elif command == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif command == 'all':
        s = {i for i in range(1, 21)}
    elif command == 'empty':
        s = set()