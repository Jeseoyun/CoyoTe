def next_word(word, start, end):
    if start > end:
        return

    min_char = '['  # Z보다 큰 아스키 코드
    min_idx = -1
    for i in range(start, end):
        if word[i] < min_char:
            min_char = word[i]
            min_idx = i

    # 모든 문자 True
    if min_idx == -1:
        return

    is_insert[min_idx] = True

    for i in range(leng):
        if is_insert[i]:
            print(word[i],end='')
    print()

    next_word(word, min_idx + 1, end)  # min_idx 기준 오른쪽
    next_word(word, start, min_idx)  # min_idx 기준 왼쪽

word = input()
# print(word)

word_split = list(word)
# print(word_split)

leng = len(word_split)
is_insert = [False] * leng

next_word(word_split, 0, leng)