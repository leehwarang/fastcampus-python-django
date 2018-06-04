students = []

student1_info = {
    "first_name" : "michelle",
    'last_name' : "lee",
    'student_no' : 7067
}

student2_info = {
    "first_name" : "frank",
    'last_name' : "park",
    'student_no' : 8898
}

student3_info = {
    "first_name" : "demi",
    'last_name' : "jung",
    'student_no' : 1234
}

student4_info = {
    "first_name" : "tod",
    'last_name' : "jung",
    'student_no' : 5678
}

students.append(student1_info)
students.append(student2_info)
students.append(student3_info)
students.append(student4_info)

#print(sorted)

#def sort_help(d): #dictionary를 받은 다음 그 dic을 student_no로 정렬해주는 함수
#    return d['student_no']
#sorted_students= sorted(students, key=sort_help)
sorted_students= sorted(students, key=lambda x: x['student_no'])
print(sorted_students)

'''
함수를 만드는건 동일하지만, 함수가 들어갈 변수 이름을 지정하지 않는다.
함수를 선언하는 것은 전역 변수로 작용하기 때문에 공간을 많이 차지함.
따라서 프로그램 중 한 번 사용하기 위해 만든 함수들은 lambda 함수로 만든다. 
사용법: 파라미터를 콜론 앞에 쓰고, 콜론 뒤에는 리턴할 연산자를 넣는다. 
'''

# a = lambda x : x+1 
# print(a(2))
# #print((lambda x : x+1) (2)) 변수에 담지 않고 바로 호출하는 방법
# b = lambda x, y, z : x + y + z
# print(b(1,2,3))
# c = lambda x, y : (x ** 2) + (y ** 2)
# print(c(2,3))

# (lambda x : True if x%2 == 0 else False)(10)
# (lambda *x: sum(x)) (1,2,3,4,5)




