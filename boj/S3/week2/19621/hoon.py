# 백준: 회의실 배정2
# 아빠한테 회의랑 회의실을 물려받았다는게 뭘까... 요즘은 문제도 AI로 만드는건가...

# 임의의 회의 k가 k-1과 k+1과 겹치고 나머지는 겹치지 않는다는 건
# 직관적으로 해석했을 경우 동시에 회의를 진행할 수 없이 하나만 진행해야한다는 거고
# 논리적으로 구현 과정을 설명했을 때, 회의 k를 고르면 k-1과 k+1을 선택할 수 없다?? 는 그런 느낌임.
import sys
inputf = sys.stdin.readline

def main():
    num = int(inputf())
    
    # 입력 받고
    meeting_info = []
    for _ in range(num):
        data = list(map(int, inputf().split()))
        meeting_info.append(data)

    # 시작을 기준으로 정렬
    meeting_info.sort(key = lambda input_data:input_data[0])

    # print(meeting_info)

    # 회의가 하나 예외처리
    if num == 1:
        print(meeting_info[0][2])
        return

    # 점화식을 세워보면 dp[k]를 선택하면 dp[k-2]와 현재 값을 더하는거고, dp[k]를 선택하지 않으면 dp[k-1]을 그대로 가져옴
    dp = [0] * num
    dp[0] = meeting_info[0][2]
    dp[1] = max(meeting_info[0][2], meeting_info[1][2])
    # dp[1] = meeting_info[1][2]

    for i in range(2, num):
        dp[i] = max(dp[i-1], dp[i-2] + meeting_info[i][2])
    
    print(dp[num-1])

if __name__ == "__main__":
    main()