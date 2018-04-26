'''
5-4: isnumeric() 함수 구현
숫자로 변환 가능한 string인지 알려주는 isnumeric()함수를 만들어 보세요. 
ex. '1.234'.isnumeric() -> True
    '1.2ab'.isnumeric() -> False

<해결 아이디어> 
isnumeric함수는 문자열에 숫자만 포함된 경우는 True, 그렇지 않으면 False를 반환. 
'''

def check_numeric(str):
    try:
        float(str) #숫자로만 이루어져있다는 것은 float로 변환할 수 있다는 것을 의미
        return True
    except:
        return False
            
print(check_numeric("12345")) #true 
print(check_numeric("12345hello")) #false
print(check_numeric("123.5")) #true
print(check_numeric("123.ab")) #false






