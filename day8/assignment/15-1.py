'''
lambda함수와 map, filter, reduce 중 1개 이상을 써서
다음 리스트를 아래와 같이 바꾸세요. 
origin_list = list(range(1, 10+1))
'''
from functools import reduce

origin_list = list(range(1, 10+1))

#1번. [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

list1 = list(filter(lambda x: x > 2, origin_list))
list1.append(11)
list1.append(12)
print(list1)

#2번. [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list2 = list(map(lambda x: x**2, origin_list))
print(list2)

#3번. [64, 81, 100]

list3 = list(filter(lambda x : x > 60, list2))
print(list3)

#4번. [55]

list4 = list(filter(lambda x : x < 30, list2))
value = reduce(lambda x, y : x + y, list4)
emptied_list = []
emptied_list.append(value)
print(emptied_list)

#5번. 55

list5 = list(filter(lambda x : x < 30, list2))
list5 = reduce(lambda x, y : x + y, list5)
print(list5)


