print('--파이썬과 mysql연동----')
'''
--아나콘다 설치 후 path 설정--
제어판 -> 시스템 및 보안 > 시스템 > 고급 시스템 설정 (시스템 속성 고급 탭)
> 환경변수 > 사용자 > path 선택 후 편집
경로를 추가  (새로 만들기해서)

파이참 setting > + 버튼 눌러서 install packing
----------------------------------------
cmd창 또는 anaconda3 prompt(관리자권한으로 실행)
pip install pymysql
명령어로 설치하자

pip install pymysql
'''
'''
#pymysql설치
pip install pymysql
#절차
[1]MariaDB연결: 연결자이름=pymysql.connect(연결옵션)
[2] 커서생성: 커서명=연결자이름.cursor()
[3] sql문 실행: 커서명.execute("SQL문장")
[4] 트랜잭션 완료: 연결자이름.commit()
[5] MariaDB 연결 종료: 연결자이름.close()
'''
import pymysql

config={
    'host':'localhost',
    'user':'root',
    'password':'1234',
    'database':'schooldb',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

con=pymysql.connect(**config)
print(con)