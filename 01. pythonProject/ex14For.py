print('중첩 for loop문-----')
'''
3행5열 for 루프 이용해서 출력해보기
*****
*****
*****
'''
for i in range(3):
    for k in range(5):
        print("*",end='')
    print()
'''
[2] 중첩 for루프 이용해서 아래와 같은 모양을 출력하세요
'''
# *
# **
# ***
# ****
# *****

for b in range(6):
    print('*'*b)
print('-'*30)
for i in range(5):
    for j in range(5):
        if i>=j:
            print("*",end='')
    print()
print('-'*30)

for i in range(5):
    for j in range(5):
        if i+j<=4:
            print("*",end='')
    print()
'''
(0,0),(0,1),(0,2),(0,3),(0,4)
(1,0),(1,1),(1,2),(1,3),(1,4)
(2,0),(2,1),(2,2),(2,3),(2,4)
(3,0),(3,1),(3,2),(3,3),(3,4)
(4,0),(4,1),(4,2),(4,3),(4,4)


[3] 중첩 for루프 이용해서 아래와 같은 모양을 출력하세요
'''
'''
*****
****
***
**
*
'''
print('#'*30)
count=5
for i in reversed(range(0, 5)):
    for j in range(0, count):
        print("*", end = "")
    count -= 1
    print()
    
'''
[4] 트리 모양으로 출력해보세요
	  *
	 ***
	*****
   *******
   
   4행 7열
(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)
(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)
(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6)
(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)  
'''
print('#'*30)
for i in range(4):
    for k in range(7):
        if i+k>=3 and k-i<=3:
            print('*',end='')
        else:
            print(' ',end="")
    print()
'''
[5] 구구단 전체 출력하기
'''
for i in range(1, 10):
    for k in range(2, 10):
        print('{}x{}={}'.format(k,i, i*k), end='\t')
    print()
