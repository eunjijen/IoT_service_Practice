print('if문--------------')
'''
[1] 주 제어문
    <1> 조건문 : if, if ~ else, 다중 if문(if ~ elif ~ elif ...else )
    <2> 반복문 : for 루프문, while 루프문
[2] 보조 제어문 : 단독으로는 사용 불가. 주 제어문과 함께 사용된다
    break, continue
    ------------------------------
    <1> if문
    if 조건식:
        실행문
    <2> if ~ els문
    if 조건식:
        실행문1
    else:
        실행문2
        
    조건식이 True이면 실행문1을 실행하고, False이면 실행문2를 실행한다        
        
    * 들여쓰기에 주의하자
        
    <3> 다중 if문 
    if 조건식:
        실행문1
    elif 조건식:
        실행문2
    elif ...
    
    else:    
        실행문n
    
'''
a=-10
if a>0:
    print(a,'는 양수입니다')
    print('~~~~~~~')
print('The End###') #조건과 상관없이 실행되는 문장

val=int(input('정수값을 입력하세요: '))
'''
val이 양수이면 "양수입니다", 음수이거나 0이면 "음수 또는 0입니다" 출력하세요
'''
if val>0:
    s="양수입니다"
else:
    s="음수 또는 0입니다"
print(s)
'''
    양수 : "Positive"
    음수인 경우와 
    0인 경우를 나눠서
    "Negative"
    "Zero"
'''
if val>0:
    s="Postive"
else:
    if val==0:
        s="Zero"
    else:
        s="Negative"
print(s)

if val>0:
    s="양수"
elif val<0:
    s="음수"
else:
    s="0"
print(s)