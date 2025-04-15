# 사각형을 2개로 분리해서 너비 계산
# 사각형에서는 잘리지 않은 긴 변이 2개 존재 긴 변을 기준으로 인덱스 +1, +5는 높이 값
# 긴변 인덱스를 기준으로 +2, +4너비 값으로 본다면 큰 밭을 작은 직사각형 2개로 분리 가능
# 각 직사각형의 넓이를 계산 후 더해서 당근 개수 곱하기

k = int(input())

len_list = [list(map(int, input().split())) for _ in range(6)]

standard_idx = 0
for i in range(6):
    if len_list[i % 6][1] == len_list[(i + 2) % 6][1] + len_list[(i + 4) % 6][1]:
        standard_idx = i
        break

h1 = len_list[(standard_idx + 1) % 6][1]
h2 = len_list[(standard_idx + 5) % 6][1]

w1 = len_list[(standard_idx + 2) % 6][1]
w2 = len_list[(standard_idx + 4) % 6][1]

total = h1 * w1 + h2 * w2
print(total*k)
