print('---list---------')
'''
자료구조: list, tuple, dict, set
[1] 리스트
    - 요소들이 순서대로 저장된다=> 시퀀스 자료형: list, tuple
    - 인덱스로 관리된다
    - 저장되는 요소들의 자료형(타입)이 같을 필요는 없다
    - 리스트는 저장된 값을 변경할 수 있다.(mutable)
        <cf> 튜플의 경우는 변경 불가(immutable)
    - 중복 데이터 저장 가능    
'''
#리스트 생성은  [  ] 를 이용한다
# []: 대괄호 => list
# {}: 중괄호 => dict, set
# (): 소괄호 => tuple
list1=[] #빈 리스트
list2=[1,2,3,4] #정수 리스트
list3=["Hello","Hi","Bye"] #문자열 리스트
list4=['A',100,3.14,True,False] #혼합 리스트

print(list1, type(list1))
print(list2, '길이: ', len(list2))
print(list3, '길이: ', len(list3))
print(list4, '길이: ', len(list4))

print(list3[0])
print(list3[2], list3[-1], list3[len(list3)-1])

# for루프 이용해서 list4에 저장된 값을 출력하세요
for item in list4:
    print(item,end=' ')
print()

#list slicing
'''
리스트명[start:end[:step]]
    start부터 (end-1)까지 slicing한다
'''
lst=[10,20,30,'Hello','Python',False]
print('#'*50)
print(lst)
print('lst[3:4]=', lst[3:4])
print('lst[3:5]=', lst[3:5])

print('lst[0:3]=', lst[0:3])
print('lst[:3]=', lst[:3])

# 'Hello'부터 끝까지 조각내서 출력하기
print('lst[3:]=', lst[3:])

print('---주민 번호 추출-----')
jumin='130301-3012345'
#문자열도 기본적으로 리스트
'''
[1] 생년월일을 추출해서
13년 3월 1일 생입니다
'''
print(f'{jumin[0:2]}년 {jumin[2:4]}월 {jumin[4:6]}일 생입니다.')
#[2]주민번호에서 생년월일 이후 '-'를 제외한
# 문자열을 출력하세요
print(jumin[7:])
# [3] 주민번호에서 짝수/홀수 위치의 문자들을 출력하세요
print(jumin)
print(jumin[0::2])
print(jumin[1::2])
#[4] 주민번호를 역순으로 출력하세요
print(jumin[::-1])
print(jumin[14::-1])

print(jumin[20]) #IndexError발생
print(jumin[:20]) #slicing을 이용하면 에러 나지 않음
