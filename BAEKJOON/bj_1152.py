# 1152 단어의 개수
sentence = input().split()
# 방법 1
#print(len(sentence))
# 방법 2
count = 0
for _ in sentence:
    count += 1
print(count)