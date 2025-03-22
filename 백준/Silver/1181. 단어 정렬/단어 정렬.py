N = int(input())
arr= [0] * N
for i in range(N):
    arr[i] = input().strip()

arr= set(arr)
arr = sorted(arr, key = lambda x:(len(x), x))
for word in arr:
    print(word)