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

class Account(Wallet):
    def __init__(self, name, account_number): #부모 클래스의 오버라이드 
        self.account_number = account_number
        super().__init__(name) #부모가 가지고 있는 함수 호출 
    
    def __str__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __repr__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __add__(self, another):
        return self.money + another.money 
    
    def __call__(self):
        print("호출되었습니다.")

    def send_money(self, money, to):
        if self.money > money:
            to.money += money
            self.money -= money
            print("{}원을 {}에게 보냈습니다.".format(money, to.owner))
            self.print_now_money()
 
        