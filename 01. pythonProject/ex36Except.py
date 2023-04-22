print('##프로그램 시작####')
try:
    n=int(input('정수를 입력하세요: '))
    print('Hello '*n)
    print('Python '+str(n))
    print(10//n)
except TypeError as e:
    print('자료유형을 잘못 사용하고 있어요!! ',e)
except ValueError as e:
    print('입력값 오류!! 정수를 입력해야 해요!! ',e)
except Exception as e: #Exception으로 잡으면 모든 예외가 다 여기서 잡힌다.
    print('예상치 못한 기타 에러 발생!! ', e)
else:
    #try절에서 예외가 발생하지 않았을 경우 실행될 코드
    print('프로그램이 에러없이 잘 수행됐어요~~')
finally:
    #finally절은 예외가 발생해도 반드시 1번은 실행하고 넘어간다
    print("**반드시 실행되어야 할 코드***")
    
print('##프로그램 종료####')

'''
발생가능한 에러를 모두 try~except로 처리해보세요
'''