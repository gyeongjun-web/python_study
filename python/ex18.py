weight,height=eval(input('체중과 키를 입력하시오:'))
std=(height-100)*(0.9)

if weight>std:
    print('과체중입니다.')
elif weight==std:
    print('표준 체중입니다.')
else:
    print('저체중 입니다.')
    