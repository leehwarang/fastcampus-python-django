raw_list = list(range(1, 100+1))

map(lambda x: 'fizzbuzz' if x%15 == 0 else
 ('fizz' if x%3==0 else ('buzz' if x%5 ==0 else x)), raw_list)

 print(list(result)))