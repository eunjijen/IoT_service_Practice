print('6. 멤버쉽 연산자: in, not in')
'''
in : 리스트, 튜플, 문자열에 지정한 값이 있으면 True, 없으면 False를 반환한다.
'''
lst =[5,7,3,10] #list
print(lst, type(lst))

tup=('Hello','Hi',"Allo") #tuple
print(tup, type(tup))

print(20 in lst) # False
print(3 in lst) # True

print(20 not in lst) # True
print('Hello' not in tup) # False

'''
대입연산자, 할당연산자
패킹(packing) 할당
'''
a, b =1, 'Hi'
print(a, b)
print(lst) #[5, 7, 3, 10]

v1, *v2 = lst
print(v1)
print(v2)

*v1, v2 = lst
print(v1)# [5, 7, 3]
print(v2)  # 10

s='apple'
print(s, type(s))
print('pl' in s)

