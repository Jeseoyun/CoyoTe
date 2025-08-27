'''

[처음 생각]

접근법
1. 인접한 각 나라간의 인구 수 차이 확인 
2. L~M 사이의 차이인지 확인
3. 이동할 수 있는 국가들 클러스터링 하기 
4. 각 나라들이 배치하게 되는 인구 평균 구하기 
5. 몇일 동안 이동이 발생하는지 확인


Quetion
1. 몇일 동안 인구 이동이 발생하는지 어떻게 확인할까?
2. 연합이 여러개로 나눠질 때 어떻게 처리해야할까?

- - - - - - - - - - - - - - - - - - - - - - 

[풀이법]

전략: 모든 구역에서 인구 이동 조건 만족하지 않을 때까지, BFS로 돌린다. 


[코드 어려움]
bfs _ 큐 어디에 생성하지
sm _ 첫 초기화 어디에 하지 

'''

from collections import deque

# N: 땅 한 변, L: 최저 이동 조건, R: 최대 이동 조건  
N,L,R=map(int,input().split())


# 땅
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))


# BFS
def bfs(si,sj):

    # deque 생성, 스타트 노드 큐에 넣기, 방문 체크
    q=deque()
    q.append((si,sj))
    v[si][sj]=1

    alst=[(si,sj)] # 연합 리스트
    sm=arr[si][sj] # 합계


    dij=[(0,-1),(0,1),(1,0),(-1,0)]  # 탐색 방향

    while q:

        i,j=q.popleft() 

        for di,dj in dij:
            ni=i+di
            nj=j+dj

            if 0<=ni<N and 0<=nj<N: # 범위 여부 확인
                if v[ni][nj]==0: # 방문 여부 확인
                    if abs(arr[i][j]-arr[ni][nj])>=L and abs(arr[i][j]-arr[ni][nj])<=R: # 이동 조건 여부 확인
                        q.append((ni,nj))  # q에 삽입
                        v[ni][nj]=1 # 방문 체크
                        alst.append((ni,nj))
                        sm+=arr[ni][nj]


    # bfs 들어온 좌표로 부터 연결된 연합 가능한 모든 좌표 탐색 후 종료하고 나온 시점
    # 평균값으로 연합 값들 변경 
    if len(alst)>1: # 연합인 경우
        for ti,tj in alst:
            arr[ti][tj]=sm//len(alst)
        return 1
    return 0  # 연합 없는 경우



# main 
mt=0  # 이동횟수(moving_time)
while mt<=2000:
    # 전체를 순회하면서, 미방문 -> 방문처리

    v=[[0]*N for _ in range(N)]  # 방문 체크 확인 리스트
    flag=0  # 인구이동 확인 여부

    for i in range(N):
        for j in range(N):
            if v[i][j]==0: # 방문하지 않았다면
                t=bfs(i,j) # 연합이 있었으면 1, 아니면 0반환
                if t==1:
                    flag=1


    # 인구 이동하지 않았다면 종료 
    if flag==0:
        break

    mt+=1
                


print(mt)



