print('--중첩 함수------------')
'''
중첩함수는 함수 내부에 다른 함수가 내장된 형태를 의미한다.

def 외부함수(인수):
    실행문1
    def 내부함수1():
        실행문2
        return 값1
    def 내부함수2(인수):
        실행문3
        return 값2
    return 내부함수1, 내부함수2
'''

def foo(): #outer function
    print('foo()함수')
    def bar(): #inner function
        print('bar()함수##')
    return bar

#foo()호출하기
b=foo()
# print(b)
b() #bar()가 수행됨

list1= list(range(1,101))
print(list1, type(list1))
'''
list1을 인자로 받는 함수
외부함수명: total_avg
    내부함수 : total  list1의 합계값을 구해 반환함수
    내부함수 : avg    list1의 평균값을 구해 반환함수
'''
def total_avg(data):
    print('data=',data)
    def total():
        tot_val=sum(data)
        return tot_val
    def avg(tot_val):
        av=tot_val/len(data)
        return av
    return total, avg

mtotal, mavg=total_avg(list1) # 함수 클로저
'''
외부함수가 종료되어도 객체로 만들어지기 때문에
합계, 평균을 계산하는데 사용할 수 있다. 이런 함수를 함수 클로저라고 한다
'''

result=mtotal()
print('result=',result)
ag=mavg(result)
print('ag=', ag)
