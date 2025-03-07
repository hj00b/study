# [D3] 이진수 표현 - 10726 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS) 

### 성능 요약

메모리: 67,712 KB, 시간: 517 ms, 코드길이: 221 Bytes

### 제출 일자

2025-03-07 12:31



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do

##### 참고 코드
```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mask = (1 << N) - 1
    if M & mask == mask:
        print(f"#{tc} ON")
    else :
        print(f"#{tc} OFF")
```
