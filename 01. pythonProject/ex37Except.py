print('--예외 회피하기---------')
try:
    print(9/0)
except ZeroDivisionError:
    pass
print('--프로그램 종료------')

print('---예외 발생시키기 ------')
'''
예외 발생시키기: raise를 이용해서 예외를 발생시킨다
        해당 예외가 발생했을때 처리 구문을 작성해야 한다
'''
userid=input('아이디를 입력하세요: ')
try:
    if userid=='killer':
        raise ValueError("killer는 절대로 입장할 수 없어요")
    print(userid, '님 환영합니다~~!!')
except ValueError as e:
        print(e)

def get_answer(ans):
    if ans in ['Yes','No']:
        print('>>알겠습니다<<')
    else:
        raise ValueError("입력 오류!! Yes/No 둘 중 하나를 입력해야 해요")

while True:
    ans=input('Yes 또는 No 중 하나를 입력하세요: ')
    try:
        get_answer(ans)
        print('ans=',ans)
        if ans=='Yes':
            break
    except ValueError as ex:
        print(ex)
        '''
        오류 메시지를 디버그 해야 할때 =>상세히 출력하고자 한다면
        '''
        print(f'오류 종류: {type(ex).__name__}')
        print(f'오류 발생 파일명: {__file__}')
        print(f'오류 발생 위치: {ex.__traceback__.tb_lineno} 번째 라인에서 에러 발생!!')





