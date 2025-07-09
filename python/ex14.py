a=int(input('반지름을 입력하세요:'))
pi=3.141592
area=pi*(a**2)
if a < 0:
    print('잘못된 입력입니다.')
else:
    print(area)