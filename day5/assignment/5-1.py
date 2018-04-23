'''
5-1. all, any 함수 구현
built-in function인 all, any 함수를 구현해보세요.

<해결 아이디어>
1. all 
함수에서 받은 인자가 iterable한지 검사
    case1. iterable하다면? 참
    case2. iterable하지 않다면? 거짓

2. any 
함수에서 받은 인자가 iterable한지 검사
    case1. iterable하고 & 비어 있지 않다면? 참
    case2. iterable하지 않다면? 거짓
'''

import collections

def check_all(n):
    if isinstance(n, collections.Iterable):
        return True
    else:
        return False

print(check_all(("This is string")))


def check_any(n):
    if isinstance(n, collections.Iterable):
        if not n:
            return False
        else:
            return True
    else:
        return False

print(check_any(("This is string")))


