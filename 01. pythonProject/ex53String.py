#41String.py
print('---문자열 연산과 메서드----')
s1="First String"
s2='Second String'
print(s1, type(s1))
print(s2)
# '+'연산자는 문자열 결합
print(s1+s2)
# '*' 연산자
# print(s1*s2) [x]
print(s1*3)
print(s1+str(10)) #str+int [x]

#slicing
print(s1[0]) # F
print(s1[:5]) # First
print(s1[5:])

#문자열=> immutable (불변성)
# s1[0]='A' #[x]
s='i like python i Like React.js'
print(s)
print(s.upper()) #모두 대문자로
print(s)
print(s.lower()) #소문자
'''
#capitalize() : 첫글자만 대문자로
#title() : 단어의 이니셜들을 대문자로
#count(인자) : 인자가 몇개있는지 반환한다.
'''
print(s.capitalize())
print(s.title())
'''
like 단어가 s에 몇개있는지 출력하세요
'''
print(s.upper().count('LIKE'))
print(s.lower().count('like'))
'''
find('검색어'): 검색어에 해당하는 인덱스번호를 반환한다. 없으면 -1을 반환한다
index('검색어'): 검색어에 해당하는 인덱스번호를 반환한다. 없으면 에러 발생
'''
#print(s.index('likes')) #ValueError: substring not found
print('like문자열 위치: ',s.find('like')) #2
print('like문자열 위치: ',s.lower().find('like', 5)) #16
print('likes문자열 위치: ',s.lower().find('likes')) #-1
'''
startswith('단어') : '단어'로 시작하는지 여부를 반환. True/False
endswith('단어') : '단어'로 끝나는지 여부를 반환
strip(): 좌우 공백을 제거하여 새로운 문자열을 반환
lstrip(): 왼쪽 공백 제거
rstrip(): 오른쪽 공백 제거
'''
print(s.startswith('you'))
print(s.endswith('.js'))

s2="  You like Python   "
print(s2)
print('s2의 길이: ', len(s2))
print(s2.strip(), '앞뒤 공백제거후 길이:', len(s2.strip()))
s3=s2.lstrip()
print(s3, '왼쪽 공백 제거후 길이: ',len(s3))
s3=s2.rstrip()
print(s3, '오른쪽 공백 제거후 길이: ',len(s3))
'''
split(sep) : sep기준으로 쪼개어 반환
'sep'.join(): sep를 구분자로 합치기
'''
msg='python this is a python! good job!~~'
print(msg)
word=msg.split() #list로 반환. 공백을 구분자로 쪼갬
print(word)
word=msg.split(sep='!')
print(word)
'''
python이 몇개 있는지 출력하기
'''
# word=msg.split()
print(word[0].count('python'))
print(msg.count('python'))
word=msg.split()
print(word)
print(" ".join(word))
print('#'.join(word))

'''
isdigit()
isalpha()
isalnum() : 알파벳 + 숫자
isspace()
isupper()
islower()
istitle() : 문자열이 title형식인가?
'''
s='ABC'
print(s.isalpha(), s.isalnum(), s.islower(),s.isspace())

my=['test.txt','run.py','Hello.java','Except.py']
'''
#[1] 반복문 돌면서 '.' 를 기준으로 분리해서 확장자를 제외한 파일명을 출력하세요
'''
for w in my:
    # print(w)
    file=w.split('.') #list로 반환
    print(file[0])
'''
#[2] .py파일만 골라서 출력하기
'''
for w in my:
    # print(w, type(w))
    if w.endswith('.py'):
        print(w)