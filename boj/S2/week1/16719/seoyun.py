def dfs(s, start, result):
    if not s:
        return

    target = min(s)
    idx = s.index(target)
    result[start+idx] = target  # 원래 문자 위치에 끼워넣기
    print("".join(result))

    dfs(s[idx+1:], start+idx+1, result) # 오른쪽 먼저 처리
    dfs(s[:idx], start, result) # 이후 왼쪽 처리


def main():
    s = list(input())
    result = [''] * len(s)
    dfs(s, 0, result)


if __name__ == "__main__":
    main()