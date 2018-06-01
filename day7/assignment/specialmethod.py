'''
Python Special Method
: Python의 모든 데이터는 '객체'이다. 지금은 int, string등의 기본 클래스의 객체를 만들어서 간단하게 test하였지만,
사용자가 직접 class를 만들고 클래스 내부에서 special method를 변형하여 사용할 수 있다. 
'''

#1. __call__(self): 클래스의 객체가 함수처럼 호출되면 실행된다.(일반적으로 클래스는 함수처럼 호출될 수 없다.)

class Hello:
    def __init__(self, name):
        self.name = name
        
    def __call__(self):
        print("hello {}".format(self.name))

michelle = Hello('michelle') #Hello 클래스의 객체 생성 
michelle()

#2~6은 컨테이너(list, tuple, dictionary) 관리를 위한 special method.
#이에 대한 원소를 조회, 갱신, 삭제를 추가하는 함수들을 말한다. 

#2. __len__(self): 객체의 길이를 반환한다. 

a = [1,2,3]
print(a.__len__())
print(len(a)) #__len__을 구현했기 때문에, len(객체)를 사용할 수 있다. 

#3. __contains__(self, item): Container 타입 내의 포함 여부 확인

a = [1,2,3]
b = {'name': 'michelle', 'age':26, 'job':'contents developer'}

print(a.__contains__(2)) #True
print(b.__contains__('name')) #True

#4. __getitem__(self, key): 객체에서 []연산자를 사용하여 조회 할때의 동작 

a = [4,5,6]
print(a.__getitem__(0)) #a[0]과 동일
print(a.__getitem__(2)) #a[2]와 동일

#5. __setitem__(self, key, value) : : 객체에서 [] 연산자를 사용해서 변수를 지정할때 동작

a = [4,5,6]
print(a.__setitem__(0,7)) #a[0] = 7과 동일
print(a.__setitem__(2,8)) #a[2] = 8과 동일

#6. __delitem__(self, key): del object[]를 동작

a = [4,5,6]
a.__delitem__(0)

#7~10까지는 산술 연산자 
#7. __add__(self, other) : x+y 연산을 정의

a = 3
a.__add__(3) #6

#8. __sub__(self, other) : x-y 연산을 정의

a = 3
a.__sub__(3) #0

#9. __mul__(self, other) : x*y 연산을 정의

a = 3
a.__mul__(3)

#10. __truediv__(self, other) : x/y 연산을 정의

a = 5 
a.__truediv__(5) #1
a.__truediv__(4) #1.25

#11~15까지는 비교 연산자 
#11. __eq__(self, other): ==에 대한 동작 정의

a.__eq__(5) #True
a.__eq__(6) #False

#12. __ne__(self, other): !=에 대한 동작 정의 

a.__ne__(5) #False
a.__ne__(6) #True

#13. __lt__(self, other): <에 대한 동작 정의 

a.__lt__(3) #False
a.__lt__(7) #True 

#14. __gt__(self, other): >에 대한 동작 정의 

a.__gt__(3) #True
a.__gt__(7) #False

#15. __ge__(self, other): >=에 대한 동작 정의 

a.__ge__(2) #True
a.__ge__(3) #True
a.__ge__(4) #False


