class Car:
    color=""
    speed=0

    def __init__(self):
        color=""
        speed=0

    def upspeed(self,value):
        self.speed+=value

    def downspeed(self,value):
        self.speed-=value

    #추가된 메서드
    def printMessage(self):
        print("시험 출력이다.")

myCar1=Car()
myCar2=Car()
myCar3=Car()
myCar1.color="빨강"
myCar1.speed=0
myCar2.color="파랑"
myCar2.speed=0
myCar3.color="노랑"
myCar3.speed=0


#인스턴스 변수
myCar1.upspeed(30)
myCar1.downspeed(60)
myCar1.printMessage()

myCar2.upspeed(30)
myCar2.downspeed(60)
myCar2.printMessage()

myCar3.upspeed(30)
myCar3.downspeed(60)
myCar3.printMessage()
        