import random
import time

# 단어 리스트
words = ['여름','장마','소나기','사과','수박','참외','김치찌개','고기','라면','신라면','진라면','너구리',
         '메밀소바','스시','스테이크','카레','나베','삼각김밥']

high_score = 0  # 최고 점수 저장

# 카운트다운 함수
def countdown():
    print("\n게임 시작까지...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("시작!\n")

# 게임 실행 함수
def play_game():
    global high_score  # 전역 최고 점수 사용
    score = 0
    life = 3

    countdown()

    while life > 0:
        word = random.choice(words)
        print(f'제시어: {word}')

        start_time = time.time()
        user_input = input('입력: ')
        end_time = time.time()

        elapsed = end_time - start_time

        if user_input == word and elapsed <= 2:
            print('✅ 성공! +1점\n')
            score += 1
        else:
            life -= 1
            reason = '시간초과' if elapsed > 2 else '오답'
            print(f'❌ 실패 ({reason}) 생명 -1 (남은 생명: {life})\n')

    print('💀 게임 오버!')
    print(f'이번 게임 점수: {score}')

    if score > high_score:
        high_score = score
        print("🎉 최고 점수 갱신!")

    print(f'🏆 현재 최고 점수: {high_score}')

# 메인 루프
print('== 한글 단어 게임 ==')
print('제시된 단어를 2초 안에 정확히 입력하세요.')
print('틀리거나 늦으면 생명이 줄어듭니다. 생명은 3개!\n')

while True:
    input("▶ 게임을 시작하려면 Enter 키를 누르세요!")
    play_game()

    retry = input("\n다시 시작하시겠습니까? (Y/N): ").strip().lower()
    if retry != 'y':
        print("\n🎮 게임을 종료합니다. 감사합니다!")
        break