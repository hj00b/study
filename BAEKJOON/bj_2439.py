# 별 찍기 문제
num = int(input())
blank = num - 1
for star in range(1, num +1): 
    print(" "*blank + "*"*star)
    blank -= 1

#스터디원 답

N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)

"""
--배울점
각 변수의 관계를 잘 이해하고 필요한 곳에 변수를 사용할 것
가능하다면 이미 있는 변수를 사용할 것
코드를 작성하기 전에 가능한 구조를 파악할 것

"""