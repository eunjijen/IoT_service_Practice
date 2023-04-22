print('--재귀함수----------')
'''
재귀함수(rescursion)란?
- 함수내부에서 자기 자신을 호출하는 함수를 말한다.
- 재귀 함수를 구성하고자 할때는
  반드시 종료 조건을 걸어야 한다 [주의사항]
'''

def a():
    print('a함수입니다...')
    a() #자기 함수를 호출
#a()

# 5 4 3 2 1
for i in reversed(range(1,6)):
    print(i, end=" ")
print('\n',"#"*30)

def counter(num):
    if num==1: #종료 조건
        print(num, end=' ')
        return 1
    print(num, end=" ")
    return counter(num-1)

counter(5)

'''
factorial
5! = 5x4x3x2x1 =120

재귀함수로 구현해보세요
함수명 : fact1
'''

def fact1(num) :
   if num==1 :
       print(num,end="=")
       return 1
   print(num, end="x")
   return num*fact1(num-1)

print(fact1(5))

total=1
def fact11(total,n):
    if (n == 1):
        print(f'{n} = {total}')
        return 1
    print(n, end = 'x')
    total *= n
    return fact11(total,n-1)

fact11(total,5)


total = 1
def fact(n):
    print(n, end = 'x')
    global total
    total *= n
    if (n == 1):
        print(f'{n} = {total}')
        return 1
    return fact(n-1)

print(fact1(5))
