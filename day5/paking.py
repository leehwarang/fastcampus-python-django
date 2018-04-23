'''
*와 ** 모두 인자를 paking해주는 것.
*는 위치 인자를 paking하여 tuple로 만들어줌. 
**는 키워드 인자를 paking하여 dictionary로 만들어줌.
'''


#위치 인자 paking 예제
def sum_all(*args):
    return(sum(args))

print(sum_all(1,2,3,4,5,6,7,7,8))

#키워드 인자 paking 예제
def print_f_name(**kwargs):
    for key in kwargs:
      print(key, '의 이름은', kwargs[key])
print_f_name(father="홍길동",mother="김영희",sister="하니",brother="둘리", cat="나비")




