# ex41FileRead.py
print('--file readline()-----')
'''
ex01Hello.py파일을 읽어서 콘솔에 출력하되,
앞에 줄번호를 붙여서 출력합시다
1: print('Hello')
2: print('Python')

readlin()함수는 줄단위로 읽어들인다. 반복문과 함께 사용해야 함
'''
try:
    with open('ex01Hello.py','r', encoding='utf8') as f:
        num=1
        while True:
            line=f.readline()
            if not line: #읽은 내용이 없다면 반복문 벗어나기
                break
            print(str(num)+": "+line,end='')
            num+=1
except:
    print('파일 읽는 중 에러 발생!!')