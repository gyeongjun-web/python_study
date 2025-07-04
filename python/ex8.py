num=int(input('정수:'))

fourth=num//1000
third=(num%1000)//100
second=(num%100)//10
first=(num%10)

sum=fourth+third+second+first
print(sum)