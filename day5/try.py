'''
try:
    Error 발생할 우려가 있는 코드
except:
    Error 발생시 작동하는 코드
'''

try:
    num = input('숫자를 입력하세요.')
    num = int(num)
    print(10/num)
except (ValueError, ZeroDivisionError):
        print("숫자를 숫자 키로 입력하세요.. 한글로 말구요.. 영어도 안돼요..")

#모든 error를 try-except으로 처리하게 된다면, 나중에 디버깅을 하기 어려워짐.
#except는 예상한 error만 써줘야 한다. 

