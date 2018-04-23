
# 리스트 unpaking 예제
# def sum_all(*args): # 1.unpaking되어 있는 것을 다시 함수에서 paking하여 tuple로 만든다. 
#     print(sum(args)) # 3.tuple값들을 더한다. 

# print(sum_all(*[1,2,3,4,5,6,7,7,8,9,10])) # 1.리스트로 paking되어 있는 것을 unpaking해서 넘겨준다.


#딕셔너리 unpaking 예제
family_dict = {
    "father": "홍길동",
    "mother": "김영희", 
    "sister": "김태희", 
    "cat" : "코카"
}

def print_f_name(**kwargs): #2.unpaking했던 것을 다시 paking. 
    for key in kwargs:
      print(key, '의 이름은', kwargs[key])

print_f_name(**family_dict) # 1.dictionary로 paking되어 있는 것을 unpaking해서 넘겨준다. 

'''
paking: 키워드 인자인지, 위치 인자인지 중요한 것이 아니라 함수를 정의할 때 들어 올 인자가 몇개인지 모를 경우에 사용함. 
unpaking: 함수에 어떤 값을 넘길 때 paking되어 있는 값을 풀어서 넘기기 위해 사용함.
    - unpaking되어 있는 데이터 형식: 딕셔너리, 리스트 등등.. 
    - 따라서 int형을 인자로 보낼 때는 함수를 정의할 때 paking만 하면 되는 것이고, 
      list나 dictionary형을 인자로 보낼 때는 함수를 호출 할 때 unpaking, 정의할 때 paking해서 사용한다.
'''
