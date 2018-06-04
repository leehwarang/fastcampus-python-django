'''
@decorator 만들기

1)다음 모듈의 기능을 이용하여서 함수의 실행 시간을 측정하는 데코레이터를 만들어보세요.

from time import time

start_time = time()
end_time = time()
executed_time = end_time - start_time
'''

from time import time

def check_time(func):
    def new_func(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print('함수가 걸린 시간은:', end_time - start_time)
        return result
    return new_func

@check_time
def sum_1_to_n(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

@check_time
def gauss_sum(n):
    return (n * (n+1))/2



result = sum_1_to_n(12340000)
print(result)
result2 = gauss_sum(12340000)
print(result2)



