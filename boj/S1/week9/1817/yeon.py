# 짐 챙기는 숌

"""
n 번 째 박스를 채울 차례에서 1 ~ n-1 번 박스는 고려하지 않는다? 
Example:

    Input:
    3 12 
    6 7 6 

    Expected Output:
    2

    Answer:
    3

"""
def main():

    # 책의 개수 N, 박스 감당 가능 무게 M
    N, M = map(int, input().split())
    
    # 책이 없는 경우
    if N == 0:
        print(0)
        return
    
    boxes = 1  # 필요한 박스의 개수 (최소 1개 필요)
    books = list(map(int, input().split()))  # 책의 무게

    curr_weight = 0 # 현재 박스에 담긴 책의 무게 
    for book_weight in books:
        # 현재 박스에 담긴 책의 무게 + 현재 책의 무게가 박스의 감당 가능 무게를 초과하는 경우
        if curr_weight + book_weight > M:
            boxes += 1  # 박스 개수 증가
            curr_weight = book_weight  # 현재 박스에 담긴 책의 무게를 현재 책의 무게로 초기화
        # 현재 박스에 담긴 책의 무게 + 현재 책의 무게가 박스의 감당 가능 무게를 초과하지 않는 경우
        else:
            curr_weight += book_weight
    print(boxes)  # 필요한 박스의 개수 출력
    
if __name__=='__main__':
    main()