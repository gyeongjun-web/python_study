import random
import time

word=['여름','장마','소나기','사과','수박','참외','김치찌개','고기','라면','신라면','진라면','너구리'
,'메밀소바','스시','스테끼','카레','나베','삼각김밥']

score=0
life=3

print('==한글 단어 게임== ')
print('제한시간은 2초')

input('enter를 누르면 시작\n')

print('\n게임 시작까지...')
for i in range(3,0,-1):
    print(i)
    time.sleep(1)

print('시작\n')

while life>0:
    words=random.choice(word)
    print(f'제시어:{words}')

    start_time=time.time()
    user_input=input('입력:')
    end_time=time.time()

    elapsed=end_time-start_time

    if user_input==words and elapsed<=2:
        print('+1:')
        score+=1
    else:
        life-=1
        reason='시간초과' if elapsed>2 else "오답"
        print(f'실패 ({reason})생명 -1 (남은 생명:{life})\n')


print('게임 오버')
print(f'최종점수:{score}')
input('\n enter 키를 누르면 종료')