def get_unique_sorted_list():
    number=[]
    print('정수를 입력하세요. 입력을 마치려면 done을 입력하세요.')

    while True:
        value=input('정수:')
        if value.lower()=='done':
            break
        try:
            num=int(value)
            number.append(num)
        except ValueError:
            print('정수만 입력하시오:')

    unique_sorted=sorted(set(number))

    return unique_sorted

result=get_unique_sorted_list()
print('정렬된 중복 제거 리스트:',result)

