# 머리 톡톡 
# https://www.acmicpc.net/problem/1241

import sys

inputf = sys.stdin.readline
MILLION = 1000000

def get_divisors(n):
    """
    약수 구하기 
    설명: 
    n의 제곱근까지 순회하면서 약수를 구하고, 
    약수의 짝이 있으면 두 수를 모두 약수로 추가 
    예를 들어, 12의 약수는 1, 2, 3, 4, 6, 12 이지만, 
    12의 제곱근인 3을 기준으로 1, 2, 3, 4, 6, 12 이렇게 구할 수 있음 
    이렇게 하면 약수를 중복해서 구하지 않음 
    """
    divisors = []
    for i in range(1, int(n**0.5) + 1):  # 1부터 n의 제곱근까지 순회 
        if n % i == 0:  # i 가 n의 약수인 경우 
            divisors.append(i)  # 약수 리스트에 i 추가  
            if i != n // i:  # i 와 n // i 가 다른 경우     
                divisors.append(n // i)  # 약수 리스트에 n // i 추가 
    return divisors

def main():

    N = int(inputf())  # 학생 수 

    numbers = [0 for _ in range(MILLION + 1)]  # numbers[i] 에는 몇 명의 학생이 i를 머리위에 썼는지 나타냄 
    # students = [int(inputf()) for _ in range(N)]  # 학생이 자신의 머리에 쓴 숫자 -> numbers 사용하기 위해 주석 
    students = list()  # 학생이 자신의 머리에 쓴 숫자
    for _ in range(N):
        n = int(inputf())
        students.append(n)  # 학생이 자기 자신 머리에 쓴 숫자 추가 
        numbers[n] += 1  # 학생이 자기 자신 머리에 쓴 숫자 개수 추가 
    
    for student in students:  # 각 학생 순회 
        divisors = get_divisors(student)  # 약수 리스트 구하기 
        toktok = 0  # 현재 학생이 머리 친 학생 수 
        for divisor in divisors:  # 약수 순회 
            toktok += numbers[divisor]  # 머리 톡톡 친 학생 수 추가 
        print(toktok - 1)  # 자기 자신 제외             
    
    return

if __name__=='__main__':
    main()