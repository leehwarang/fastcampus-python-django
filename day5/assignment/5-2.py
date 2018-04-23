'''
5-2. 재귀함수
: 제곱근의 근사값을 구하는 재귀함수를 만들어 보세요.

어떤 0보다 큰 a를 선정한 뒤, a의 제곱이 b와 한없이 가깝다면 a는 b의 제곱근
                       그게 아니라면 a를 (a+(b/a))/2로 바꾼 뒤 다시 함수를 호출해 보세요.
'''

def check_square_root(a, b):
    if abs(b-a**2) <= 0.00001:
        return a
    else:
        a = (a+(b/a))/2
        return check_square_root(a, b)
        
print(check_square_root(5, 30))
print(check_square_root(2, 4))
print(check_square_root(7, 50))
