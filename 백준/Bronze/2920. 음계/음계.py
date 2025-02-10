num_lst = list(map(int, input().split()))
asc = list(range(1,9))
des = list(range(8,0,-1))
if num_lst == asc:
    print("ascending")
elif num_lst == des:
    print("descending")
else:
    print("mixed")