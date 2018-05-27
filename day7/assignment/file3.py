'''
Bank Class의 기능 추가하기
1. 은행 대표 번호와 계좌 번호 생성 패턴을 입력하여 인스턴스 생성하기(o.k)
2. 계좌 번호 생성하는 메소드를 만들어서 입력받은 패턴대로 랜덤한 숫자를 더하여 계좌번호 리턴(o.k)
3. 업그레이드된 Account Class에서 인스턴스 생성시 bank 인스턴스도 같이 입력, bank instance의 메소드를 사용하여 계좌번호 자동생성되게 조정
4. 에러 발생시 은행 대표번호가 출력되어 문의 가능하도록 입력처리
'''

from random import randint

class Wallet:
    money = 0

    #Wallet 클래스의 객체를 만들었을 때, 처음으로? 자동으로? 실행되는 메소드.
    def __init__(self, name): 
        print("{}님 환영합니다.".format(name))
        self.owner = name

    def __str__(self):
        return '{}의 지갑입니다.'.format(self.owner)
    
    def __repr__(self):
        return '{}의 지갑입니다.'.format(self.owner)

    def print_owner_name(self): #모든 메소드에 첫 번째로 들어오는 파라미터는 자동적으로 self
        print("owner name is", self.owner)

    def print_now_money(self):
        print("현재 잔액은 {0}입니다.".format(self.money))

    def spend(self, m):
        if self.money < m: 
            print("돈이 부족합니다.")
            self.print_now_money()
        else: 
            self.money -= m
            print("{}를 지출했습니다.".format(m))
            self.print_now_money()
            
    def income(self, m):
        self.money += m
        self.print_now_money()
    
class Account(Wallet): #Wallet클래스를 상속 받음. 
    def __init__(self, name, account_number, password, bank): #부모 클래스의 오버라이드 
        self.account_number = account_number
        self.password = password
        self.bank = bank
        super().__init__(name) #부모가 가지고 있는 함수 호출 
    
    def __str__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __repr__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __add__(self, another):
        if self.owner == another.owner:
            self.money += another.money 
            print("계좌 통합이 완료 되었습니다.")
            print("잔액: {}".format(self.money))
        else:
            print("두 계좌의 소유주가 다릅니다.")
    
    def __call__(self):
        print("호출되었습니다.")

    def send_money(self, money, to): #to에 객체명(f_account)를 적어야함
        input_password = input("패스워드를 입력하세요.")
        if self.password == input_password:
            print("확인 되었습니다.")
            if self.money > money:
                if self.bank == to.bank:
                    pass
                else:
                    self.money -= 500 #수수료 500원 추가
                    print("수수료 500원이 차감됩니다.")
                to.money += money
                self.money -= money
                print("{}원을 {}에게 보냈습니다.".format(money, to.owner))
                self.print_now_money()
            else:
                print("잔액이 부족합니다.")
        else: 
            print("패스워드를 다시 입력해주세요.")
    

class Bank():
    def __init__(self, tel, pattern): 
        self.tel = tel
        self.account_number = self.random_account_number(pattern) #class내에 있는 함수를 호출 할 때는 앞에 self를 붙여야 실행됨. 
        
        
    def random_account_number(self, pattern): #함수의 인자에는 항상 self 써줘야함. 
        pattern2 = pattern.split('-')
        list = []

        for i in pattern2:
            n = 0
            for j in range(len(i)):
                if j == 0:
                    n += randint(0,9)*1
                elif j == 1:
                    n += randint(0,9)*10
                elif j == 2:
                    n += randint(0,9)*100
                elif j == 3:
                    n += randint(0,9)*1000
            list.append(n)
        
        num1 = str(list[0])
        num2 = str(list[1])
        num3 = str(list[2]) 

        account_number = num1+"-"+num2+"-"+num3 
        return account_number 


        