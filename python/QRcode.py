#QRcode로 문제 내고 맞추기
import qrcode
import random
proverbs=[('호랑이 굴에','들어가도 정신만 차리면 산다'),('등잔 밑이','어둡다'),('가는 말이 고와야','오는 말이 곱다'),('고생 끝에','낙이 온다'),('원숭이도','나무에서 떨어진다')
        ,('티끌모아','태산'),('백문이','불여일견'),('똥 묻은 개가','겨 묻은 개 나무란다'),('바늘 도둑이','소 도둑 된다'),('낫 놓고','기역자도 모른다'),('까마귀 날자','배 떨어진다'),
         ('발 없는 말이','천 리 간다'),('천리길도','한 걸음 부터'),('소 잃고','외양간 고친다'),('개천에서','용난다'),('돌 다리도','두드려 보고 건넌다'),
         ('낮 말은 새가 듣고','밤 말은 쥐가 듣는다'),('돈 앞에','장사없다'),('튀기면','신발도 맛있다'),('백짓장도','맞들면 낫다')]

print('속담 맞추기 게임')
input('enter를 누르면 시작')
score=0
total=0
while True:
    front,back=random.choice(proverbs)
    print(f'\n정답을 적어 넣으세요:\n____{back}')
    input('준비가 되면 enter를 누르셈')
    print(f'속담:\'___{back}\'')
    answer=input('앞 부분을 입력하세요:').strip()
    total+=1
    if answer==front:
        print('정답\n')
        score +=1
    else:#힌트 제공
        hint=front[0]
        length=len(front)
        print(f'오답 힌트는',{hint},'로 시작.(총 {length} 글자)')
        answer2=input('힌트를 보고 다시 입력하셈:').strip()
        if answer2==front:
            print('정답\n')
            score+=1
        else:
            print(f'오답. 정답은:\'{front}\'\n')

    accuracy=(score/total)*100    
    print(f'현재 점수:{score}/{total}')
    print(f'정확도:,{accuracy:.2f}%\n')

    cont=input('계속 하시겠습니까?(y/n):').lower()
    if cont !='y':
        break
   
print(f'\n게임 종료! 최종 점수:{score}/{total}')
print(f'총 정확도:{accuracy:.2f}%')


img.qrcode.make(front+" "+back)
img.save(f"proverb_{total}.png")