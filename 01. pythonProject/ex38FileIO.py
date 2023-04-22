print('--FileIO 파일 입출력----')
'''
파일 사용 절차
1. 파일 열기 : open()한뒤 read / 파일쓰기: open()한뒤 write
2. 파일 읽기/쓰기/수정
3. 파일 닫기
#파일모드
[1] r : read mode (기본값) 읽기 전용 모드
[2] w : write mode : 쓰기 전용모드
[3] a : append mode 파일 마지막에 새로운 데이터를 추가하는 모드
[4] t : text mode 파일 데이터를 텍스트 파일로 인식하고 입출력함 (기본값)
[5] b : binary mode : 바이너리 파일로 인식하고 입출력함
[6] x : : 쓰기용 파일을 새로 만들어서 연다.(기존 파일이 있으면 error)
'''
import os

print('현재 디렉토리1: ', os.getcwd())
#현재 디렉토리 변경
os.chdir("C:/Temp")
print('현재 디렉토리2: ', os.getcwd())

#[1] 파일 열기: open(파일명, 모드)
#[2] 파일 쓰기: write()
#[3] 파일 닫기: close()

f=open('readme2.txt','a') # w 모드는 write mode 쓰기 모드 w모드는 파일이 존재하면 그 파일에 덮어쓰기를 한다
'''
x 모드는 이미 있는 파일에 쓰고자 할 경우 에러를 발생시킨다
a 모드는 기존 파일에 덧붙이기(append)를 한다
'''
f.write("안녕하세요? 반갑습니다.\n")
f.write("잘 가세요~!!\n")
f.close()

print(os.getcwd(),'에 readme2.txt파일에 쓰기를 완료했어요')

'''
with open() 을 이용하면 close()를 자동으로 처리해준다
'''

# with open('파일명','모드값') as 별칭:
#     별칭.write()

with open('readme2.txt','a') as f:
    f.write("기존 파일에 덧붙이기 합니다")

print('readme2.txt파일에 쓰기 완료!!')




