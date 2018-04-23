#n! = n * (n-1) * (n-2) * ... *1

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(5))


#재귀함수 더하기
#정수 a와 n을 받아서 a에 n을 더하는 함수를 재귀함수로 만들어보세요.

def add_n(a, n):
    if n == 0:
        return a
    return 1 + add_n(a, n-1)

print(add_n(10, 7))





