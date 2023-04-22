num=100 #변수

def foo():
    myvar="지역변수 myvar"
    global hisvar #전역변수
    hisvar="전역변수 hisvar"
    print('-'*50)
    print(globals()) #전역변수들을 dict로 반환 
    print('*'*50)
    print(locals()) #지역변수들을 dict로 반환
    globals()['hisvar']='change value'
    print(globals())
if __name__ =='__main__':
    foo()