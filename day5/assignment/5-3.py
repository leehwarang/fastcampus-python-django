'''
5-3. 재귀함수
: 5-2 재귀함수 중 "한 없이 가깝다면"을 "전에 값과 변함이 없다면" 조건으로 바꿔 만들어보세요.
'''

def check_square_root(a, b):
    if (a+(b/a))/2 == a:
        return a
    else:
        a = (a+(b/a))/2
        return check_square_root(a, b)
        
print(check_square_root(5, 30))
print(check_square_root(2, 4))
print(check_square_root(7, 50))
