import random
proverbs=[('호랑이 굴에','들어가도 정신만 차리면 산다'),('등잔 밑이','어둡다'),('가는 말이 고와야','오는 말이 곱다'),('고생 끝에','낙이 온다'),('원숭이도','나무에서 떨어진다')
        ,('티끌모아','태산'),('백문이','불여일견'),('똥 묻은 개가','겨 묻은 개 나무란다'),('바늘 도둑이','소 도둑 된다'),('낫 놓고','기역자도 모른다'),('까마귀 날자','배 떨어진다'),
         ('발 없는 말이','천 리 간다'),('천리길도','한 걸음 부터'),('소 잃고','외양간 고친다'),('개천에서','용난다'),('돌 다리도','두드려 보고 건넌다'),
         ('낮 말은 새가 듣고','밤 말은 쥐가 듣는다'),('돈 앞에','장사없다'),('튀기면','신발도 맛있다'),('백짓장도','맞들면 낫다')]
print('속담 맞추기 게임')
input('enter를 누르면 시작')
score=0
for j in range(5):
    front,back=random.choice(proverbs)
    print('\n정답을 적어 넣으세요:\n')
    input('준비가 되면 enter를 누르셈')
    print(f'속담:\'{front}___\'')
    answer=input('뒷 부분을 입력하세요:').strip()

    correct=0
    for i in range(min(len(back),len(answer))):
        if answer[i]==(back)[i]:
            correct += 1

    accuracy=correct/len(back)*100
    #if answer==back:              #정.오답을 말해주는 코드
    #print('정답\n')
    #score += 1
    #else:
        #print(f'오답임. 정답은:\'{back}\'\n')
    if answer==back:
        print('정답\n')
        score +=1
    else:#힌트 제공
        hint=back[0]
        length=len(back)
        print('오답 힌트는',{hint},'로 시작.(총 {length} 글자)')
        answer=input('힌트를 보고 다시 입력하셈:').strip()
        if answer==back:
            print('정답\n')
            score+=1
        else:
            print(f'오답. 정답은:\'{back}\'\n')
        
    print(f'게임 종료 당신의 총 점수는',{score},'입니다\n')
    print(f'정확도는',{accuracy},'입니다\n')