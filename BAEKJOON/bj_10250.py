# ACM 호텔
T = int(input())

for _ in range(T):
    '''
     문제 내용 )
     높이가 H 너비가 W인 호텔에 N명의 손님을 배치
     손님은 적게 걷는 것을 선호(방 번호가 적은 것을 선호)
     방 번호가 같을 경우 낮은 층을 선호 
     1)
     N번째 층 1번방부터 N의 수를 늘려가며 배치한다고 가정하면
     층 수만큼 손님을 배치하면 다음 방 번호로 넘어간다
     해당 규칙을 수학적으로 표현하면 몫+1로 방 번호를
     나머지로 층 수를 표현할 수 있다
     2)
     몫으로 나누어 떨어지는 맨 윗층의 경우 나머지로 층 수를 
     표현할 수 없으므로 총 층 수를 저장한 변수를 통해 층 수를 표현하고
     나머지가 없으므로 몫이 방 번호가 된다.
    '''
    H, W, N = map(int, input().split())
    # 1)
    floor = N % H
    room = N // H + 1
    # 2)
    if floor == 0:
        floor = H
        room = N // H

    print( floor * 100 + room)

    # 스터디원 풀이

    # 표현은 다르지만 대다수 같은 풀이 방식 사용
    # 다른 방법으로는 if문을 사용해서 맨 윗층에 도달하면
    # 층수를 리셋시키고 방 번호를 증가시키는 방법 사용
    # 변수명을 잘 지정한다면 가독성 좋은 코드가 될 것 같다.