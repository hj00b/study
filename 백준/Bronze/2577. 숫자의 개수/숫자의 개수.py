# 02월 09일
# 백준 2577.py
# 자연수 A, B, C를 입력받아 곱한 값 저장
A, B, C = [int(input()) for _ in range(3)]
num = A * B * C
# 숫자 개수를 세기 위한 빈 리스트. 예를 들어 1의 개수는 1번 인덱스에 개수에 대한 정보 저장
num_list = [0] * 10
# num을 모두 순회할 때까지 반복
while True:
    # num의 1의 자리 수를 추출해 해당 수의 개수를 카운트
    num_list[num % 10] += 1
    # 카운트한 num의 1의 자리 수를 제거
    num = num // 10
    # 만약 num의 모든 1의 자리 숫자를 확인했다면 while문 탈출
    if num < 1 :
        break
# num_list를 순회하여 count한 개수를 출력
for i in num_list:
    print(i)
'''
코드만 보기
A, B, C = [int(input()) for _ in range(3)]
num = A * B * C
num_list = [0] * 10

while True:
    num_list[num % 10] += 1
    num = num // 10
    if num < 1 :
        break

for i in num_list:
    print(i)
'''