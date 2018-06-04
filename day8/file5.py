def make_print_start_end(func):
    def new_func(*args, **kwargs): #매개변수로 함수를 받아서 바로 실행하는 것이 아니라, 함수 안에서 함수를 실행하는 것. 
        #위치인자(*args)로 받아서 패킹을 시킨 후 튜플로 가지고 있고, 키워드 인자로 받아서 패킹 후 딕셔너리로 가지고 있음.
        print("함수가 시작됩니다.")
        result = func(*args, **kwargs) #넘길 때는 가지고 있는 튜플과 딕셔너리를 언패킹.
        print("함수가 끝났습니다.")
        return result
    return new_func #new_func()의 결과값인 result를 리턴한다. 

@make_print_start_end
def print_a_to_b(a, b, c):
    for i in range(a, b+1, c):
        if i < b:
            print(i, end=',')
        else: 
            print(i)

#new_func = make_print_start_end(print_a_to_b) #함수의 인자를 함수로 보냄으로써, 함수를 변수처럼 사용한다. 
#new_func(1, 100, 3)
print_a_to_b(1, 100, 2)

@make_print_start_end
def sum_a_to_b(a, b): 
    result = 0
    for i in range(a, b+1):
        result += i
    return result

#new_func2 = make_print_start_end(sum_a_to_b)
#print(new_func2(1, 10))
result = sum_a_to_b(1, 100)
print(result)





