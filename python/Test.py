<<<<<<< HEAD
#정경준

import random
sentence=[["나는","학교를","간다"],["나는","운동을","간다"],["나는","집으로","간다"],["나는","밥을","먹는다"],["나는","밥을","먹는다"]]
print("다음 단어들을 순서대로 조합하세요:")
score=0


for i in range(5):
    chooselist = random.choice(sentence)
    answer_right = chooselist[0] + " "  + chooselist[1] + " " + chooselist[2]
    quizSen = chooselist[:]
    random.shuffle(quizSen)
    print(f'제시어:{quizSen[0]} {quizSen[1]} {quizSen[2]}')
    print("정확한 문장을 입력하세요:")
    user_input=input('입력:')

    if user_input == answer_right:
        score+=1
        print('정답:')
    else:
        print('오답:')
print(f'성공한 횟수:{score}')



=======
#정경준

import random
sentence=[["나는","학교를","간다"],["나는","운동을","간다"],["나는","집으로","간다"],["나는","밥을","먹는다"],["나는","밥을","먹는다"]]
print("다음 단어들을 순서대로 조합하세요:")
score=0


for i in range(5):
    chooselist = random.choice(sentence)
    answer_right = chooselist[0] + " "  + chooselist[1] + " " + chooselist[2]
    quizSen = chooselist[:]
    random.shuffle(quizSen)
    print(f'제시어:{quizSen[0]} {quizSen[1]} {quizSen[2]}')
    print("정확한 문장을 입력하세요:")
    user_input=input('입력:')

    if user_input == answer_right:
        score+=1
        print('정답:')
    else:
        print('오답:')
print(f'성공한 횟수:{score}')



>>>>>>> 68e4ac71918d7d023db0284f5efd2a5cae19955f
