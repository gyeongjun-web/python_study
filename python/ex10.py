temp=int(input('현재온도'))
if 120>temp>=25:
    print('반바지 추천')
elif temp<25:
    print('긴바지 추천')
elif temp>120:
    print('자살하시오')

else:
    print('잘못된 입력')