#타자 연습 게임 코드
import random  
import time
#연습 문장들
textlist=['니가 가라 하와이','마이 뭇따 아이가','나다 이 씹새끼야','밥알이 매깨고','쫄리면 뒤지시던지','민주주의를 위하여','손은 눈보다 빠르다 하지만 걱정마라 장마담에겐 위에서 한장 아귀에겐 밑에서 한장'
          ,'이거 방탄유리야 이 씹새끼야','아이 엠 아이언맨','아임 유어 빠더','혼자야? 아니 싱글이야','두루와 두루와 이 씹새끼들아','도비는 자유에요','금방 온다 해짜나요','묻고 더블로 가','마포대교는 무너졌냐 개새끼야',
          '1억은 너무 적소 5억으로 주시오','오케이 4딸라','나 전당포 한다 금니도 받아 금니뺴고 모조리 씹어먹어주마','우리가 돈이 없지 가오가 없냐','느그 아부지 뭐하시노','그거 알아? 나 지금 되게 신나!']
print('타자연습게임입니다.')
input('엔터를 누르면 시작합니다')
#랜덤 문장 선택
a=random.choice(textlist)
print('\n다음 문장을 그대로 입력하세요:\n')
print(f'{a}\n')

input('준비되면 ENTER를 누르세요')
#시간 측정 시작
start_time=time.time()

trial = 0
while True:
    #사용자 입력 받기
    typed=input('\n입력:')
    #시간 측정 종료
    end_time=time.time()
    elapsed=end_time-start_time
    #정확도 계산

    correct=0

    for i in range(min((len(a)),len(typed))):
        if a[i] == typed[i]:
            correct += 1

    total=max(len(a),len(typed))
    accuracy=correct / len(a)*100
    speed = len(typed) / elapsed*60  #분당 타자 수(cpm)

    if accuracy==100:
        print('완료.')
        break
    else:
        print('다시.')
        trial += 1


    
#결과 출력
print('\n결과')
print(f'걸린 시간:{elapsed:.2f}초')
print(f'시도횟수:{trial:.2f}')
print(f'정확도:{accuracy:.2f}초')
print(f'타자 속도:{speed:.2f}초')