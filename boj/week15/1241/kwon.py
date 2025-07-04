import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

students = [int(input()) for _ in range(N)]
MAX_STUDENT = max(students) + 1

counter = Counter(students)
toktok = defaultdict(int)

for i in range(1, MAX_STUDENT):
    for j in range(i, MAX_STUDENT, i):
        if j in counter:
            # print(f"{i} {j} {counter[j]}\n")
            toktok[j] += counter[i]
# print(str(toktok))
# print(str(students))
print("\n".join(str(toktok[s] - 1) for s in students) + "\n")


# # 느린 풀이
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# N = int(input())

# students = [int(input()) for _ in range(N)]

# counter = [0] * N
# for i, s1 in enumerate(students):
#     for j in range(i + 1, N):
#         s2 = students[j]
#         if s1 % s2 == 0:
#             counter[i] += 1
#         if s2 % s1 == 0:
#             counter[j] += 1

# for cnt in counter:
#     print(f"{cnt}\n")