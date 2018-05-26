'''
1. 계좌 생성시에 password 지정 및 은행이름 입력.(o.k)
2. 송금시에 password 입력 및 일치하는지 확인(o.k)
3. 송금시에 같은 은행이 아닌 경우에는 수수로 -500 원 별도 부여(o.k)
4. 소유자가 같은 계좌는 + 연산자로 보유금액 합산가능
5. 소유자가 같은지 == 연산자 혹은 != 연산자로 확인가능
'''

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
    

#michelle_wallet = Wallet('michelle') #클래스를 사용해서 객체를 만들었을 때, 만들어진 자기 자신 객체를 지칭하는 self
#frank_wallet = Wallet('frank')

#print(my_wallet.owner)
#my_wallet.print_owner_name()

class Account(Wallet): #Wallet클래스를 상속 받음. 
    def __init__(self, name, account_number, password, bank): #부모 클래스의 오버라이드 
        self.account_number = account_number
        self.password = password
        self.bank = bank
        if self.name == 
        super().__init__(name) #부모가 가지고 있는 함수 호출 
    
    def __str__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __repr__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __add__(self, another):
            self.money + another.money 
    
    def __call__(self):
        print("호출되었습니다.")

    def send_money(self, money, to): #to에 객체명(f_account)를 적어야함. 
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
    


        