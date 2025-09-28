def main():
    n, w, L = map(int, input().split())  # 트럭 수, 다리 길이, 최대 하중
    a = list(map(int, input().split()))

    bridge = [0]*w
    t = 0
    curr_idx = 0

    while curr_idx < n:
        # print(t, bridge, curr_idx)
        t += 1
        bridge.pop(0)

        if sum(bridge) + a[curr_idx] <= L:
            bridge.append(a[curr_idx])
            curr_idx += 1
        else:
            bridge.append(0)

    t += w

    print(t)

if __name__ == "__main__":
    main()