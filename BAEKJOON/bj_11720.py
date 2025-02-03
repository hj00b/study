import sys
sys.stdin = open("input.txt", "r")

input()
nums = input()

num_list = []

for num in nums :
    num_list.append(int(num))

print(sum(num_list))

# 스터디원 답안 
'''
1. input 데이터 리스트로 변환 후 반복문에서 pop으로 값 출력
    반복문에서 변수를 사용하지 않을 경우 언더스코어로 처리 가능
2. 반복문을 통해 변수에 누적합을 계산
3. total = sum(int(a) for a in number)
4. 반복문이 아니라 map을 통해서 list에 int 값을 저장
'''