T = int(input())
h_arr = list(map(int, input().split()))
h_arr.sort()
for i in range(1, T):
    h_arr[i] = h_arr[i] + h_arr[i-1]
for i in range(1, T):
    h_arr[i] = h_arr[i] + h_arr[i-1]
print(h_arr[T-1])