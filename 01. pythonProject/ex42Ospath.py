#ex42Ospath.py
print('--os모듈, os.path모듈---------')
'''
os.getcwd():현재 작업 디렉터리의 위치를 반환한다.
os.chdir(path): 현재 작업 디렉터리의 위치를 변경한다.
os.listdir(path): 해당 경로에 존재하는 파일과 디렉터리의 목록을 반환한다.
                〉〉〉os.listdir(‘.’):
os.remove(path): 해당 파일을 삭제한다.
os.mkdir(path): 해당 디렉터리를 생성한다.
os.rmdir(path): 해당 디렉터리를 삭제한다.(내용이 있는 디렉터리 삭제 불가)
os.makedirs(path):여러 개의 디렉터리를 순차적으로 생성한다. 
    만약 이미 디렉터리가 있으면 예외가발생한다.
                〉〉〉os.makedirs(‘test3/test4/test5’)
os.removedirs(path): 여러 개의 디렉터리를 역순으로 삭제한다.
                〉〉〉os.removedirs(‘tesst3/test4/test5’)
os.rename(src, dst): 파일이나 디렉터리의 이름(src)을 dst로 변경한다.
                〉〉〉os.rename(‘test.txt’, ‘example.txt’)
'''
import os
print('현재 디렉토리: ',os.getcwd())
# os.chdir('C:/Temp')
# os.chdir('C:\\Temp')
os.chdir(r'C:\Temp') # raw : 주어진 문자열을 그대로 해석하란 의미
print('현재 디렉토리: ',os.getcwd())

flist=os.listdir(r'C:\Temp') #특정 디렉토리 내의 파일/디렉토리 목록을 반환한다
print(flist, type(flist))

print('#'*30)
for file in flist:
    print(file)
# os.mkdir('sample2') #sample디렉토리를 만든다 make direcory
# os.rmdir('sample') #sample디렉토리를 삭제 remove directory
# os.rename('sample2','example') #디렉토리나 파일명을 변경하고자 할때
# os.makedirs("test/sub")
# os.removedirs("test/sub")
'''         ㄷ
os.path모듈: 파일 경로를 조작하는 모듈
'''
print(os.path.abspath('readme.txt')) #파일의 절대경로 구하기
print(os.path.exists('test.txt')) #False
print(os.path.isfile('readme.txt')) #파일인지 여부 True
print(os.path.isdir('readme.txt')) #False
print(os.path.getsize('readme.txt'),'bytes') #파일 크기를 반환
files=os.path.split(r'C:\Users\TECH3-29\PycharmProjects\pythonProject\ex01Hello.py') #튜플로 반환
#split(): 디렉토리명과 파일명을 분리해준다
print('상위 디렉토리명: ', files[0])
print('파일명: ',files[1])

#join(): 디렉토리명과 파일명을 결합
print(os.path.join('C:\\Temp','test.py'))




