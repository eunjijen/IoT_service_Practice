print('--ex34Module.py-----')
'''
# 패키지
# 함수, 클래스들을 용도별로 분리해서 작성하는 것=>모듈
# 그런데, 이러한 모듈들이 모여 뒤죽 박죽 섞여 있으면
# 이해도, 활용도가 떨어짐
# 따라서, 모듈들 역시 성격에 맞게 분류해서 관리해야 할
# 필요성이 있다 => 패키지를 이용해서 모듈들을 관리함

# 파이썬에서 패키지를 만들려면
# 1) 디렉토리 생성
# 2) __init__.py 파일 생성
# 그런데, py3 이상은 __init__.py 파일 없이도
# 자동으로 패키지 인식 => py2와의 호환성을 위해 생성해 둠

# 패키지 내 함수를 호출하려면
# import 패키지명.모듈명 선언문 사용
'''
import mypkg.yourModule1

print(mypkg.yourModule1.num)

import mypkg.yourModule1 as your
print(your.num)
'''
from 패키지명.모듈명 import 함수명, 클래스명, 변수명...
'''
from mypkg.yourModule1 import num,foo
print('num=',num)

#foo() 호출해보기
# your.foo()
# mypkg.yourModule1.foo()
foo()
print('#'*50)
'''
mypkg의 yourModule2를 import해서
add(), minus(), circleArea()각각 호출해보세요
'''
import mypkg.yourModule2 as y2
y2.add(10,20)

from mypkg.yourModule2 import minus
minus(50,40)
# add(3,5) [x]

from mypkg.yourModule2 import *
'''
mypakg.yourModule2에 있는 모든 것을 가져다 사용하겠다
'''
add(3,5)
area=circleArea(8)
print('area=',area)






