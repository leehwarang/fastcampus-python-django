#file2에서 만든 dictionay를 class로 만들어봄

class Wallet: #모든 class는 Object라는 클래스를 상속 받는다. 
    def __init__(self, name): #처음 객체가 생성될 때 실행되는 메소드. 클래스 내부에서 메소드를 만들 때는 항상 처음에 self라는 파라미터를 넘겨줘야한다. 
        self.owner = name
    
    def print_owner_name(self):
        print(self.owner)

my_wallet = Wallet('michelle')

print(my_wallet.owner) #self는 즉, 만들어진 Wallet 객체인 my_wallet를 가리킨다. 


