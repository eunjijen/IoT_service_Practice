print('---list의 메소드-----')
'''
append() : 리스트 뒤부터 추가한다(덧붙이기)
insert(index, val) : 특정 index위치에 val을 삽입
index(val): 리스트에서 val값이 있는 곳의 인덱스번호를 반환한다
'''
lst=[]
print(lst)
for i in range(1, 4):
    lst.append("Python"+str(i))

print(lst)

lst.insert(1,'Hello ')
print(lst)

i=lst.index('Python2')
print('Python2의 index번호: ',i)

# Python2를 찾아서 JavaScript로 수정하세요
lst[lst.index('Python2')]='JavaScript'
print(lst)
lst[-1]="C++"
print(lst)

#리스트 원소 삭제
'''
pop() : 맨 뒤 요소부터 제거
pop(위치): 특정 위치의 요소 제거
remove(값): 삭제할 대상 값을 지정. 리스트에 동일한 요소가 여러 개 있을 때는
          인덱스가 가장 낮은 요소 하나만 제거함 
del 리스트명[인덱스] : 특정 위치의 요소를 제거함
clear() : 리스트의 모든 요소를 제거
'''
lst.pop()
print(lst)

'''
index번호가 1인 요소를 삭제하세요
'''
lst.pop(1)
print(lst)

lst.append('Python1')
print(lst)

lst.remove('Python1')
print(lst)
#del연산자 사용
del lst[0]
print(lst)

lst2=[10,20,30]
'''
리스트 합치기: extend()함수 활용
리스트1+리스트2
'''
lst.extend(lst2)
print('lst=',lst)

a=[1,2,3]
b=[4,5,6]
print(a+b)#[1, 2, 3, 4, 5, 6]
print(a) #[1,2,3]
a.extend(b)
print(a)

lst.clear()
print('lst를 clear한 뒤: ',lst)
'''
리스트의 sort()함수: 원본 데이터를 오름차순 정렬함
        내림차순 정렬 sort(reverse=True)
sorted()함수 : 정렬은 하되, 원본 리스트를 변경하지는 않음
'''
import random as rnd

for _ in range(5):
    lst.append(rnd.randint(1,50))
print(lst)
lst.sort()
# lst.sort(reverse=True)
print('sort()한 뒤의 lst-----')
print(lst) #오름차순
lst.reverse() #내림차순
print(lst)
print('sorted(lst): ',sorted(lst))
print('lst: ', lst)
'''
enumerate()함수를 이용하면 리스트항목과 인덱스도 함께 출력할 수 있다
'''
names=["영희","순희","철이","미숙"]

for i, item in enumerate(names): #i: 인덱스번호, item:요소값
    print(f'{i+1} : {item}')

'''
리스트를 카피하고자 할때 slicing사용한다
'''
arrCopy=names[:] #사본
arr=names #arr과 names변수가 같은 리스트를 참조한다
print('arrCopy: ',arrCopy) #사본
print('arr: ', arr)

arrCopy[1]="BTS"
print('names: ', names)
print('arrCopy', arrCopy)

arr[1]="Black Pink"
print('names: ',names)
print('arr: ', arr)




