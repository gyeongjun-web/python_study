n=int(input("정수를 입력하세요:"))
total_sum=0
for n in range(1,n+1):
    total_sum=(total_sum+n**2)
print(total_sum)