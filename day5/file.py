'''
위치 인자와 키워드 인자. 
다만 키워드 인자를 위치 인자의 앞에 사용할 수는 없다. 
'''

def test(a, b, c):
    print('a는 :', a)
    print('b는 :', b)
    print('c는 :', c)

test(3, c=1, b=2)