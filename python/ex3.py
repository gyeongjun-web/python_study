message="%s시간 %s분은 %s초입니다"
h=int(input('시간:'))
m=int(input('분:'))
s=(h*60*60)+(m*60)
print(message%(h,m,s))