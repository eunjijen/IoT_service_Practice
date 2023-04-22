import math

def add(a,b):
    print(a,"+",b,"=",a+b)
    return a+b

def minus(a,b):
    print(f'{a}-{b}={a-b}')
    return a-b

def circleArea(r):
    print(f'반지름이 {r}인 원의 면적: {math.pi*r*r}')
    return math.pi*r*r