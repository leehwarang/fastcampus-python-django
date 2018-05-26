MY_MONEY = [0]

def spend(m):
    if MY_MONEY[0] > m: 
        MY_MONEY[0] -= m
        print("{}를 사용했습니다. 남은 잔액 : {}".format(m, MY_MONEY[0]))
    else: 
        print("가지고 있는 돈이 부족합니다.")

def income(m):
    MY_MONEY[0] += m 
    print("{}를 벌었습니다. 남은 잔액: {}".format(m, MY_MONEY[0]))

#여러 개의 기능들을 가지고 있는 하나의 dictionary로 만듦. 
#하지만 나의 wallet만이 아닌 다른 사람들의 wallet도 만들고 싶을 때는 별개의 dictionary를 또 다시 만들어야 함 -> class의 필요성을 설명하기 위해서 dictionay를 하나의 객체처럼 만들어 본 것. 

wallet = {
    'money': MY_MONEY,
    'spend' : spend,
    'income' : income,
}

