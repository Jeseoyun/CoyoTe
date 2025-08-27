def main():
    N, M = map(int, input().split())

    book_weights = list(map(int, input().split())) if N > 0 else []

    weight_sum = 0
    box_cnt = 0
    for weight in book_weights:
        weight_sum += weight

        if weight_sum > M:  # 최대 무게를 초과했을 경우
            box_cnt += 1
            weight_sum = weight  # 다음 박스로 넘긴다
        elif weight_sum == M:  # 딱뎀일 경우
            box_cnt += 1
            weight_sum = 0  # 다음에 무게 넘기지 않아도 됨

        # print(weight, weight_sum, box_cnt)

    # 마지막에 처리해야 할 무게가 남아있을 경우 박스 하나 추가
    if weight_sum > 0:
        box_cnt += 1

    print(box_cnt)


if __name__ == "__main__":
    main()


# 문제 잘못 이해함 ;; 책이 차곡차곡 쌓여있어서 무조건 순서대로 꺼내야 한다 ;;


# from collections import deque
#
#
# def main():
#     N, M = map(int, input().split())
#     book_weights = list(map(int, input().split()))
#
#     queue = deque(sorted(book_weights))
#
#     bags = 0
#     while queue:
#         heavy_book = queue.pop()  # 현재 남은 책 중 가장 무거움
#         bags += 1
#
#         while queue:
#             light_book = queue.popleft()
#             if heavy_book + light_book <= M:
#                 heavy_book += light_book
#             else:
#                 queue.appendleft(light_book)
#                 break
#
#     print(bags)
