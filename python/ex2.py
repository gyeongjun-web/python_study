message="%s마리의 닭과 %s마리의 돼지와 %s마리의 소의 다리에 합은 %s입니다"
C=int(input('x:'))
P=int(input('y:'))
W=int(input('z:'))
a=(C*2+P*4+W*4)
print(message%(C,P,W,a))
