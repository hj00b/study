my_set = set()
for i in range(10):
    num = int(input())
    num = num % 42
    my_set.add(num)
print(len(my_set))