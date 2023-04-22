#ex39FileWrite.py
'''
파일명을 입력받으세요
무한루프 돌면서 저장할 메시지를 입력받아 해당 파일에 저장하세요
단 exit를 입력하면 무한루프를 종료시키세요
'''
fname=input('저장할 파일명을 입력하세요: ')

f=open(fname,'a')

while True:
    msg=input('파일에 저장할 내용 입력: ')
    if msg=='exit':
        break
    f.write(msg+"\n")

f.close() #파일과 노드 연결을 닫기전에 메모리 버퍼에 모아두었던 데이터를 한꺼번에 내보내기를 한다
import os
print(os.getcwd(),fname,'파일에 쓰기 완료')
print('#'*50)
'''
write() : 문자열을 파일에 쓴다
writelines() : list를 쓰고자 할때 사용
'''
lst=['Good Afternoon','!!\n','Hi','Bye\n','한글']
fname='list.txt'
with open(fname,'w+') as f:  # w+ : 쓰기모드로 쓸수도 있고 읽기도 할 수 있음을 의미
    f.writelines(lst)
    #arr=f.readlines() #파일을 읽어서 list 자료형으로 반환한다
    #print('arr=',arr, type(arr))
print(os.getcwd(),fname,'에 쓰기 완료!!')

with open(fname,'r') as f:
    data=f.readlines()
    print(data)