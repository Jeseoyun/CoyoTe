# 백준: 원판 돌리기
import sys
from collections import deque

inputf = sys.stdin.readline

def main():
    radius, size, rotate_cnt = map(int, inputf().split())

    disks = [deque(map(int, inputf().split())) for _ in range(radius)]

    for _ in range(rotate_cnt):
        #x배수인 원판 선택 move_dir 0이면 시계 1이면 반시계
        x, move_dir, dist = map(int, inputf().split())

        # 원판 회전
        for i in range(radius):
            #특정 원판 선택
            if (i + 1) % x == 0:
                # 시계 방향
                if move_dir == 0:
                    disks[i].rotate(dist)
                else:
                    disks[i].rotate(-dist)

        #2 인접하면서 같은 수
        delete_set = set()

        for i in range(radius):
            for j in range(size):
                if disks[i][j] == 0:
                    continue
                
                # 같은 원판 내에서 인접한 경우
                # 우측과 아래만 확인하면 됨. 모두 돌면서 하면 결국 그게 좌측과 위쪽을 확인한 것.
                if disks[i][j] == disks[i][(j+1) % size]:
                    delete_set.add((i, j))
                    delete_set.add((i, (j+1) % size))

                # 인접한 다른 원판과 비교
                # 얘는 끝이랑 처음이 인접하지 않음
                if i + 1 < radius and disks[i][j] == disks[i + 1][j]:
                    delete_set.add((i, j))
                    delete_set.add((i+1, j))

        if delete_set:
            # 지울 게 있으면
            for i, j in delete_set:
                disks[i][j] = 0
        
        else:
            # 지울게 없으면 숫자들 조율해야 함
            total_sum = sum(sum(disk) for disk in disks)

            #0인 값은 지워진거기 때문에 평균 계산 분모에서 빠져야 함
            total_num = 0
            for disk in disks:
                for value in disk:
                    if value > 0:
                        total_num += 1
            
            if total_num > 0:
                avg = total_sum / total_num

                for i in range(radius):
                    for j in range(size):
                        if disks[i][j] > 0:
                            if disks[i][j] > avg:
                                disks[i][j] -= 1
                            elif disks[i][j] < avg:
                                disks[i][j] += 1
   
    sum_value = sum(sum(disk) for disk in disks)
    print(sum_value)


if __name__ == "__main__":
    main()