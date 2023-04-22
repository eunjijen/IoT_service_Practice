print('--파일 읽기와 예외처리----')
fname=input('읽을 파일명을 입력: ')
'''
[1] open()
[2] read(), readline(), readlines()
[3] close()
encoding을 utf8로 지정하면 한글은 물론 세계 여러나라의 언어를 다 읽을 수 있다.
'''
try:
    f=open(fname,'rt',encoding='utf8')
    data=f.read()
    f.close()
    print('읽은 파일 내용: data=', data)
except FileNotFoundError as fe:
    print(fname,'이란 파일은 존재하지 않아요!!')
except IOError as ex:
    print('입출력 에러 발생')
print('#'*30)
'''
with open(파일명,'r') as alias:
    명령문
자동으로 파일 리소스를 닫아준다    
'''
with open('list.txt','r') as f:
    arr=f.readlines()
    print(arr, type(arr))