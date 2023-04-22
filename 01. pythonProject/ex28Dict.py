print('--딕셔너리---------')
'''
딕셔너리 변환하기
- dict()함수 활용
  리스트 속의 리스트
  리스트 속의 튜플
  튜플 속의 리스트, 튜플  값들을 dict함수로 변환할 수 있다.
'''
grade=[['혜미','A+'],['준이','B-'],['지현','D']]
print(grade, type(grade))

dgrade=dict(grade)
print(dgrade, type(dgrade))

grade2=(['혜미','A+'],['준이','B-'],['지현','D'])
dgrade2=dict(grade2)
print(dgrade2)
print('#'*50)

score_dict={'김이썬':[90,80],'이합격':[100,100],'고길동':[78,55], '박순심':[59,99]}
'''
[1]
아래와 같은 형태로 출력하기
0 김이썬 90 80 Total: 170
1 이합격 100 100 Total: 200
2 고길동 78 55 Total: xxx
3 박순심 59 99 Total: 116
'''
i=0
for name in score_dict.keys():
    score=score_dict[name]
    total=sum(score)
    print(i, name, score[0], score[1], 'Total: ',total)
    i+=1
print('-'*30)
print(score_dict.items()) #dict_items
'''
dict.items()활용=> dict_items 클래스유형
enumerat()활용
'''
for i, (k,v) in enumerate(score_dict.items()):
    print(i, k, v[0], v[1], 'Total: ',sum(v), 'Average: ', sum(v)/len(v))

'''
# [2] 응용 실습 예제
이름, 연락처, 주소를 입력받아
입력받은 정보로 딕셔너리를 생성하고
한꺼번에 해당 정보를 출력하는 프로그램을 작성하세요
---------Menu----------------------
1. 주소록 등록  2. 주소록 출력  3. 종료
-------------------------------------
1번 입력시 이름, 연락처, 주소를 입력받기==> 딕셔너리에 저장
'''
user = dict(이름='', 연락처='', 주소='')
lst=[]
while True:
    menu = input('''---------Menu----------------------
1. 주소록 등록  2. 주소록 출력  3. 종료
-------------------------------------\n''')
    if menu == '1':
        user = dict(이름='', 연락처='', 주소='')
        for i in user:
            user[i]=input(f'{i}\n정보를 입력해주세요. : ')
        lst.append(user)
        print(user['이름'],'님의 정보가 저장되었어요~')
    elif menu == '2':
        # print(user, type(user))
        for u in lst:
            print(u)
    elif menu == '3':
        break
    else:
        print('올바른 숫자를 입력해주세요')