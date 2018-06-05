'''
문제: 데코레이터를 만들어 사용할 때 wraps은 어떠한 기능을 하는지, 
사용한 경우/사용하지 않는 경우 예제를 만들어서 설명해보세요. 
'''

from functools import wraps

def without_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@without_wraps
def my_func_a():
    """Here is my_func_a doc string text."""
    pass

@with_wraps
def my_func_b():
    """Here is my_func_b doc string text."""
    pass

print(my_func_a.__doc__)
print(my_func_a.__name__)
print(my_func_b.__doc__)
print(my_func_b.__name__)


'''
데코레이터만 사용하면 디버깅과 같이 객체 내부를 조사하는 도구가 이상하게 동작할 수 있다. 
예를 들어, my_func_a 함수의 내용은 None이 아니고, my_func_a 함수의 이름은 wrapper가 아니다.
이는 데코레이터인 wrapper 함수가 인자로 보내진 함수 my_func_a를 감싸기 때문에, 객체의 내부 정부가 wrapper 함수에 맞게 변경되기 때문이다.

이런 문제를 해결하기 위해 wraps을 사용하고, wraps을 적용하면 객체의 내부 정보(메타 데이터)가 모두 외부 함수로 복사된다. 



'''








