import math

radius=input("원의 반지름을 입력하세요")

if radius.replace('.','',1).isdigit():
    radius = float(radius)

    if radius > 0:
        area = math.pi*radius**2
        print(f"반지름이 {radius}인 원의 넓이:{area:.2f}")
    else:
        print("반지름은 0보다 커야 합니다.")

else:
    print("유효한 숫자를 입력하세요.")