import random
randomword=[("행복하다"),("친절하다"),("자전거"),("비행기"),("컴퓨터"),("동물원"),("이야기하다"),("공부하다"),("음식점"),("대학교"),("사진기"),("휴대전화")
            ,("운동화"),("버스정류장"),("냉장고")]

score=0
total=0
print(f'환영합니다\n')
print(f'시작하려면 ENTER를 누르세요\n')

while True:
    qword=random.choice(randomword)
    print(f'정답을 입력하세요\n')
