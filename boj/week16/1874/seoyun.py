def main():
    n = int(input())
    target = [int(input()) for _ in range(n)]
    stack = []
    result = []
    operation = []
    impossible = False

    current_num = 1

    while target != result:
        while current_num <= target[len(result)]:
            stack.append(current_num)
            current_num += 1
            operation.append("+")

        if stack and stack[-1] == target[len(result)]:
            result.append(stack.pop(-1))
            operation.append("-")
        else:
            impossible = True
            break

    if not impossible:
        print(*operation, sep="\n")
    else:
        print("NO")


if __name__ == "__main__":
    main()