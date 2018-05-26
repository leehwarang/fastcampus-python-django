def print_hello(name):
    print("Hello", name)

print_hello("michelle")

print_hello_name = print_hello #함수는 변수에 넣어서 호출할 수 있다. 

print_hello_name("michelle")

func_list = [print_hello, 1, 2] #함수는 리스트에 넣어서 호출할 수 있다. 

func_list[0]("michelle")

func_dict = {
    'func': print_hello
}

func_dict['func']("michelle") #함수는 딕셔너리에 넣어서 호출할 수 있다.

 