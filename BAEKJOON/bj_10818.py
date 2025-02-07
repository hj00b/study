# 10818 최소, 최대
T = int(input())
num_list = list(map(int, input().split()))

# 방법 1 
# print(f'{min(num_list)} {max(num_list)}')

# 방법 2
min = num_list[0]
max = num_list[0]
for num in num_list:
    if min > num:
        min = num
    if max < num:
        max = num
print(min, max)