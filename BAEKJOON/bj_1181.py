# 문자열 정렬, 문자열을 길이순, 문자순으로 정렬, 중복 제거
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
words = []
for i in range(n) :
    words.append(input())
words = set(words)
words = list(words)

words.sort(key=len)

def ord_comparison(words_list, i , rep):
    if len(words_list[i]) > rep and ord(words_list[i][rep]) == ord(words_list[i+1][rep]):
        return ord_comparison(words_list, i, rep+1)
    elif ord(words_list[i][rep]) > ord(words_list[i+1][rep]):
        return True
    return False

for j in range(len(words)):
    for i in range(len(words) -j -1):
        if len(words[i])<len(words[i+1]) :
            continue
        if ord_comparison(words, i, 0):
            words[i], words[i+1] = words[i+1], words[i]

                
print(words)
