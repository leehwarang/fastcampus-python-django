'''
dir()을 이용한 int의 내장된 메소드 확인
'''
import pprint
pprint.pprint(dir(int))

#Part1. 객체의 표현

__new__(cls, ...]) #새로운 인스턴스를 만들 때 처음으로 실행되는 메소드
__init__(self[, ...]) #인스턴스가 __new__로 생성되고 나서 호출되는 메소드
__str__(self) #객체를 나타내는 비공식적인 문자열이지만 객체를 이해하기 쉽게 표현할 수 있는 문자열 
__repr__(self) #객체를 나타내는 공식적인 문자열 
__format__(self) #객체를 나타내는 format을 지정하고 싶을 때 사용

#Part2. 속성 관리

__getattribute__(self, name) #객체의 속성을 호출 할 때 무조건 호출되는 함수. 만약 이 메소드가 재정의 되어있다면 __getattr__은 호출되지 않으므로 명시적으로 호출해야 하거나 AttributeError를 발생시켜야 한다. 
__setattr__(self, name, value) #객체의 속성을 변경할 때 호출되는 함수. 
__delattr__(self, name) #객체의 속성을 del 키워드로 지울 때 호출되는 함수
__dir__(self) #객체가 가지고 있는 모든 속성을 보여주는 함수

#Part3. 단항 연산자

__neg__(self) # -object를 정의한다. 
__pos__(self) # +object를 정의한다. 
__abs__(self) #절댓값 출력
__invert__(self) #비트연산 ~object를 정의

#Part4. 비교 연산자

__lt__(self, other) # x<y
__le__(self, other) # x<=y
__gt__(self, other) #x>y
__ge__(self, other) #x>=y
__eq__(self, other) #x==y
__ne__(self, other) #x!=y

#Part5. 산술 연산자

__add__(self, other) #x+y
__radd__(self, other) #x+y의 역순 연산자 
__sub__(self, other) #x-y
__rsub__(self, other) #x-y의 역순 연산자 
__mul__(self, other) #x*y
__rmul__(self, other) #x*y의 역순 연산자 
__truediv__(self, other) #x/y
__rtruediv__(self, other) #x/y의 역순 연산자 
__floordiv__(self, other) #x//y
__rfloordiv__(self, other) #x//y의 역순 연산자 
__mod__(self, other) #x%y
__rmod__(self, other) #x%y의 역순 연산자 
__divmod__(self, other) #첫 번째 인자를 두 번째 인자로 나눈 뒤, 몫과 나머지를 반환
__rdivmod__(self, other) 
__pow__(self, other) #x**y
__rpow__(self, other) #x**y의 역순 연산
__round__(self[, n]) #반올림 



#Part6. 비트 연산자와 논리 연산자
__lshift__(self, other) #x<<y 시프트 연산 
__rlshift__(self, other) #x<<y 시프트 역순 연산
__rshift__(self, other) #x>>y 시프트 연산 
__rrshift__(self, other) #x>>y 시프트 역순 연산
__and__(self, other) #x&y연산
__rand__(self, other) #x&y의 역순 연산
__or__(self, other) #x|y 연산  
__ror__(self, other) #x|y의 역순 연산 
__xor__(self, other) #x^y의 연산  
__rxor__(self, other) #x^y의 역순 연산 

#Part7. 타입 변환

__bool__(self) #bool()을 통해 호출되는 연산  
__hash__(self) #hash()를 통해 호출되는 연산. 정수를 반환
__index__(self) #slice expression에 객체가 사용될 때 사용할 정수의 형태 정의 
__float__(self) #실수 변환 
__ceil__

#기타

n.bit_length() #실제 비트의 길이를 출력 
n.conjugate() #복소수 n의 켤레 복소수를 출력 
n.imag #복소수 n의 허수를 출력
n.denominator #n의 분모를 출력  
n. numerator #n의 분자를 출력
n.real #n의 실수값을 출력 

#아직 못 찾은 함수 

__class__
__doc__
__floor__ 
__getnewargs__
__init_subclass__
__reduce__
__reduce_ex__
__sizeof__ 
__subclasshook__ 
__trunc__
to_bytes 
from_bytes



