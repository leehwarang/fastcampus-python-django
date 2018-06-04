from functools import reduce

a = [1,2,3,4]

result = reduce(lambda x, y: x+y, a) #a라는 리스트 안에 있는 값 중 2개(x, y)를 받고, 더한 값을 return. 그리고 return값과 다른 값을 더하고.. 반복. 
#map과 filter는 리스트를 반환하지만 reduce는 값을 반환한다.
print(result)
