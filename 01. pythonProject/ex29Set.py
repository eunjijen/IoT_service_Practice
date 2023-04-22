print('---set--------------')
'''
set 
- non-sequence data (순서없는 자료구조)
- index는 없다 (무순서)
- 데이터 중복을 허용하지 않음
- {} 중괄호를 이용해서 표기, set()함수 이용
- 추가,삭제,수정,집합연산 등이 가능함
'''
# help(set)
st1={} #=> 비어있는 딕셔너리
print(st1, type(st1))  #{} <class 'dict'>
st2=set() # 빈 셋을 생성하려면 set()함수를 활용한다
print(st2, type(st2))

st3={'h','e','l','l','o'}
print(st3, type(st3)) #{'e', 'o', 'l', 'h'} <class 'set'>

'''
list, tuple을 set()함수를 이용해 set으로 변환할 수 있다
'''
st4=set([1,4,6,1,5,6,9])
print(st4)
print(len(st4))

st5=set((11,22,44))
print(st5, type(st5))

#for in 루프로 st5 저장값 출력하기
for v in st5:
    print(v, end=' ')
print()
'''
추가: add()
삭제: remove(value), discard(value), pop()
'''
st5.add('Bye')
print(st5)
st5.add('bye')
print(st5)

#Bye를 삭제하기
st5.remove('Bye')
print(st5)
# st5.remove('Hello') #KeyError발생
st5.discard('Hello') #없는 값을 삭제하려 해도 에러가 나진 않음
print(st5)
'''
수정: update()
'''
st5.update(['Hello','Hi'])
print(st5)
'''
집합 연산을 할 수 있다.
- 합집합: |
- 교집합: &
- 차집합: -
- 여집합: ^
'''
s1={1,3,5,7}
s2={3,7,9,12,15}
print('s1=',s1)
print('s2=',s2)
print('s1 | s2 합집합: ', s1|s2)
print('s1 & s2 교집합: ', s1&s2)
print('s1 - s2 차집합: ', s1-s2)
print('s1 ^ s2 여집합: ', s1^s2)

print('---함수를 이용한 집합연산-------')
'''
union(): 합집합
intersection(): 교집합
difference() : 차집합
symmetric_difference(): 여집합
'''
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))




