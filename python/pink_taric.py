#https://www.pygame.org/docs/ref/display.html

import pygame

#초기화
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('PYGAME!')
clock=pygame.time.Clock()

img=pygame.image.load('pinktaric.jfif')
#img=pygame.transform.scale(img,(300,300))#파일 최적화 방법


FONT=pygame.font.SysFont('malgun gothic',48)
text=FONT.render('Intel',True,(255,255,255))
x=300
y=0
x1 = 150
y1 = 150

while True:
    screen.fill((0,0,0))#r.g.b 색상

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            elif event.key==pygame.K_LEFT:
                x1-=10
            elif event.key==pygame.K_RIGHT:
                x1+=10
            elif event.key==pygame.K_UP:
                y1-=10
            elif event.key==pygame.K_DOWN:
                y1+=10


    y+=1
    if y>600:
        y=0

    screen.blit(img,(x1,y1))
    screen.blit(text,(x,y))

    pygame.display.update()

    clock.tick(30)