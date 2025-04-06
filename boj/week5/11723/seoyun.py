# class SetOperation_v1:
#     def __init__(self):
#         self.S = set()
#
#     def add(self, x):
#         self.S.add(x)
#
#     def remove(self, x):
#         self.S.discard(x)  # remove 사용 시 key error 발생 가능성
#
#     def check(self, x):
#         print(1 if x in self.S else 0)
#
#     def toggle(self, x):
#         if x in self.S:
#             self.remove(x)
#         else:
#             self.add(x)
#
#     def all(self):
#         self.S = {i+1 for i in range(20)}
#
#     def empty(self):
#         self.S = set()
#
#
# class SetOperation_v2:
#     def __init__(self, max_len):
#         self.max_len = max_len
#         self.S_bit = [0]*max_len  # 20자리 비트를 0으로 초기화
#
#     def add(self, x):
#         self.S_bit[x-1] = 1
#
#     def remove(self, x):
#         self.S_bit[x-1] = 0
#
#     def check(self, x):
#         print(self.S_bit[x-1])
#
#     def toggle(self, x):
#         self.S_bit[x-1] ^= 1  # 1과 XOR 연산 시 무조건 비트 반전
#
#     def all(self):
#         self.S_bit = [1]*self.max_len
#
#     def empty(self):
#         self.S_bit = [0]*self.max_len


class SetOperation:
    def __init__(self):
        self.S_bit = 0  # 00000000000000000000

    def add(self, x):
        self.S_bit |= 1 << (x-1)

    def remove(self, x):
        self.S_bit &= ~(1 << (x-1))

    def toggle(self, x):
        self.S_bit ^= (1 << (x-1))

    def check(self, x):
        print(1 if self.S_bit & (1 << (x - 1)) else 0)

    def all(self):
        self.S_bit = (1 << 20) - 1

    def empty(self):
        self.S_bit = 0


# def main():
#     M = int(input())  # 연산 실행 횟수
#     SO = SetOperation()
#
#     oper_dict = {
#         "add": SO.add,
#         "remove": SO.remove,
#         "toggle": SO.toggle,
#         "check": SO.check,
#         "all": SO.all,
#         "empty": SO.empty
#     }
#
#     for _ in range(M):
#         oper, *num = input().split()
#         num = map(int, num)
#         oper_dict[oper](*num)


def main():
    import sys
    input = sys.stdin.readline
    M = int(input())
    SO = SetOperation()

    for _ in range(M):
        parts = input().split()
        oper = parts[0]
        if len(parts) == 2:
            num = int(parts[1])
            getattr(SO, oper)(num)
        else:
            getattr(SO, oper)()


if __name__ == "__main__":
    main()