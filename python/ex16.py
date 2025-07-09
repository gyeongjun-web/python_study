import random
computer=random.randint(1,3)

choice=int(input('선택하시오(1:가위 2:바위 3:보)'))
print('컴퓨터의 선택 (1:가위 2:바위 3:보):',computer)

if choice==1:
    if computer==1:
        print('컴퓨터와 비겼음')
    elif computer==2:
        print('컴퓨터가 이겼음')
    else:
        print('컴퓨터가 졌음')
elif choice==2:
    if computer==1:
        print('컴퓨터가 졌음')
    elif computer==2:
        print('컴퓨터와 비겼음')
    else:
        print('컴퓨터가 이겼음')
elif choice==3:
    if computer==1:
        print('컴퓨터가 이겼음')
    elif computer==2:
        print('컴퓨터가 졌음')
    else:
        print('컴퓨터와 비겼음')