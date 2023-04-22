print('---dict----------')
'''
자료 구조
    - 순서 자료구조(sequence data) : list, tuple
    - 비순서 자료구조(non-sequence data): dict, set
dict (Dictionary) 
    - Key값과 Value값을 매핑해서 저장하는 자료구조
    - {key : value} 형태
    - key값은 중복을 허용하지 않음
      value값은 중복 가능
    - 무순서
    - key를 이용해서 요소를 추가, 삭제, 수정 가능
    - key를 이용해서 검색하므로 검색 속도가 빠름  
'''
dic1={} #빈 딕셔너리
#[1] {key:value}
dic2={'id':20230203,'Python':'A','C':'B','Database':'C'}
#[2] dict()함수를 이용하는 방법
lst=[('산','mountain'),('바다','sea'),('하늘','sky')]
#[3] dict(key=value, key2=value2,...)
'''
대입연산자(=)를 사용해서 딕셔너리를 만들때는 key가 문자열이어야 한다
'''

dic4=dict(one=1, two=2, 셋=3, four='4') #혼합 딕셔너리

print(dic1, type(dic1))
print(dic2, type(dic2))
print(lst, type(lst))

dic3=dict(lst)
print(dic3, type(dic3))
'''
# 딕서너리 변환하기
# 리스트 속에 리스트나 튜플의 값을,
# 튜플 속에 리스트나 튜플의 값을
# key와 value로 나란히 입력하면,
# dict함수로 딕셔너리로 변환할 수 있다.
'''
print(dic4, type(dic4))
'''[주의]
딕셔너리의 key값은 정수,문자열,실수 등도 사용 가능하지만,
list나 dict와 같이 변경할 수 있는 타입(mutable type)값은
사용할 수 없다
'''
dic5={100:'hundred',20.5:'실수'}
# dic6={100:'hundred',20.5:'실수',[1,2,3]:(1,2,3)} #[x]
dic6={100:'hundred',20.5:'실수',(1,2,3):[1,2,3]} #[0]
print(dic5)
print(dic6)

# 회원정보를 dict로 선언하기     변수명: user
# key : 이름, 아이디, 비번, 이메일, 성적(국/영/수)

user={'name':'홍길동','userid':'hong','passwd':'asdf','email':'hong@a.b.c', 'score':[80,99,65]}
print(user)
'''
조회: 변수명[키], 변수명.get(키)
'''
print(user['name'])
print(user['userid'])
print(user['score'])

print('-'*30)
print(user.get('name'), user.get('email'), user.get('passwd'))
print(f'''
    국어: {user['score'][0]}
    영어: {user['score'][1]}
    수학: {user.get('score')[2]}
''')
# 존재하지 않는 키값을 지정 시
# print(user['zipcode']) #KeyError: 'zipcode'
print(user.get('zipcode')) #에러는 발생하지 않는다. None이라는 값을 반환한다
'''
딕셔너리에 데이터 추가/수정/삭제
- 추가 : d[새key]='새로운값'
- 수정 : d[key]='수정할값'
- 삭제 : del d[key], d.pop(key)
- 모두 삭제: clear()
'''
# zipcode에 25512값을 새로 추가하기
user['zipcode']=25521
print(user)
# userid를 'myhong'으로 수정하기
user['userid']='myhong'
print(user)
# score 삭제하기
del user['score']
print(user)
'''
del연산자로 삭제 시 해당 키가 없으면 에러 발생
'''
# del user['blood'] #KeyError: 'blood'

user.pop('zipcode')
print(user)
'''
pop(key) : key에 해당하는 값을 삭제하고 삭제한 값을 반환
pop(key, 대체값) : key값이 없을 때 대체할 값을 반환 
'''
# user.pop('blood') #KeyError: 'blood'
print(user.pop('blood',None)) #None  에러발생하지 않음
print(user)

# user.clear()
# print('모두 삭제 후: ', user)

'''
keys() : dict의 모든 키값들을 반환한다 dict_keys
values(): dict의 모든 밸류 값들을 반환한다
- key값을 알면 value는 자동으로 따라옴
- value값으로는 key값을 알아낼 수 없다
'''
print(user.keys())
print(user.values())


# for in loop이용해서 user의 키값들만 출력하기
for k in user.keys():
    print(f'{k} : {user[k]}, {user.get(k)}')

for v in user.values():
    print(v)