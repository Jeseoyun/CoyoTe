gear1 = list(map(int, list(input().strip())))
gear2 = list(map(int, list(input().strip())))

len1 = len(gear1)
len2 = len(gear2)

if len1 > len2:
    gear1, gear2 = gear2, gear1
    len1, len2 = len2, len1

min_total_length = len1 + len2

for start in range(-len1 + 1, len2):
    
    for i in range(len1):
        gear2_idx = start + i
        if 0 <= gear2_idx < len2:
            # 두 개의 이가 맞물리면 안됨
            if gear1[i] == 2 and gear2[gear2_idx] == 2:
                break

    else:
        current_length = max(len2, start + len1) - min(0, start)
        min_total_length = min(min_total_length, current_length)

print(min_total_length)