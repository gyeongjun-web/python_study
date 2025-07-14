def key_dict():
    result={}
    for x in range(1,11):
        key=x*x
        result[key]=x
    return result

squre_dict=key_dict()
print('제곱을 key로 갖는 딕셔너리:',squre_dict)