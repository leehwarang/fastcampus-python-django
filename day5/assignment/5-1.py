'''
5-1. all, any 함수 구현
built-in function인 all, any 함수를 구현해보세요.

<해결 아이디어>
1. all 
: all함수는 리스트, 튜플, 문자열 등과 같이 반복 가능한 자료형(iterable)을 입력 인수로 받는다. 
이 때, 자료형 안의 요소가 모두 참이거나 요소가 하나도 없으면 True를 반환한다. 

2. any 
: 요소 중 하나라도 참이 있으면 True를 반환한다. 
'''
 
def check_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(check_all([1, 2, 3, 4])) #true
print(check_all([1, 2, 3, 0])) #false
print(check_all("python")) #true 
print(check_all([])) 


def check_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(check_any([2,3,4])) #true
print(check_any([1, 2, 3, 0])) #true
print(check_all("python")) #true
print(check_any([])) #false 




