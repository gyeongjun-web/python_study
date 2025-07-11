import random
import qrcode

proverbs = [
    ('호랑이 굴에', '들어가도 정신만 차리면 산다'),
    ('등잔 밑이', '어둡다'),
    # ... 나머지 속담들 ...
]

print('속담 맞추기 게임 시작!')
input('시작하려면 Enter를 누르세요.')

score = 0
total = 0

while True:
    front, back = random.choice(proverbs)  # ← 여기 꼭 먼저 해야 함 (이게 15번째 줄이라 가정)
    
    print(f"\n속담: '___ {back}'")  # ← 여기서 back 변수 정상 출력됨
    
    answer = input("앞부분을 입력하세요: ").strip()
    total += 1

    if answer == front:
        print("정답입니다!\n")
        score += 1
    else:
        print(f"오답입니다. 정답은 '{front}'입니다.\n")

    print(f"현재 점수: {score}/{total}\n")

    cont = input("계속 하시겠습니까? (y/n): ").lower()
    if cont != 'y':
        break

print(f"게임 종료! 최종 점수: {score}/{total}")