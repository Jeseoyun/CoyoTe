def main():
    top_gear = input()
    bot_gear = input()

    if len(top_gear) >= len(bot_gear):
        long, short = top_gear, bot_gear
    else:
        long, short = bot_gear, top_gear

    long = list(map(int, list(long)))
    short = list(map(int, list(short)))

    right_padded_long = long + [0]*len(short)
    # print(long)

    min_result = float('inf')
    found = False

    for start_idx in range(len(right_padded_long)):
        # print("start_idx:", start_idx)
        for i in range(len(short)):
            # print("i:", i)
            if right_padded_long[start_idx+i] + short[i] > 3:
                break
            if i == len(short)-1:
                min_result = min(min_result, max(len(right_padded_long)-len(short), start_idx + len(short)))
                found = True
                break
        if found:
            break

    found = False

    reversed_long = long[::-1]
    reversed_short = short[::-1]
    reversed_padded_long = reversed_long + [0]*len(reversed_short)

    for start_idx in range(len(reversed_padded_long)):
        for i in range(len(reversed_short)):
            if reversed_padded_long[start_idx+i] + reversed_short[i] > 3:
                break
            if i == len(reversed_short)-1:
                min_result = min(min_result, max(len(reversed_padded_long)-len(reversed_short), start_idx + len(reversed_short)))
                found = True
                break
        if found:
            break
    print(min_result)

if __name__ == "__main__":
    main()