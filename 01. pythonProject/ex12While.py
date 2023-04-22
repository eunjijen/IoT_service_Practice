print('중첩 while문-------------')
'''
    while 조건식:
        while 조건식:
            실행문1
            증감식1
        증감식2
------------------
3행5열
*****
*****
*****        
'''
row=1
while row<=3:
    col=1
    while col <=5:
        print("*", end="")
        col+=1
    row+=1
    print() #줄바꿈
print('#'*50)

#[1] 사용자가 입력한 문자열을 그대로 출력하는
#앵무새 프로그램을 작성
#단,'quit'라고 입력하면 실행을 중단
while True:
    string=input('입력하세요: ')
    print(string)
    if string=='quit' or string=='QUIT':
        print('잘가세요~')
        break
#[2] while루프문을 중첩해서 구구단 전체를 출력해보기
'''
2x1=2   3x1=3.....      9x1=9
2x2=4   3x2=6   ....    9x2=18
...
2x9=18  3x9=27  ...     9x9=81
'''
x = 1
while(x < 10): #행의 조건  9행
    y=2
    while(y < 10): # 열의 조건  9열  ===>y=10까지 증가
        print(f'{y} X {x} = {x * y}', end = '\t')
        y += 1
    x += 1
    print()