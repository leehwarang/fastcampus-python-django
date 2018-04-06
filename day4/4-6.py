#4-6-1
'''
결과: [1,2,3,4,5,6]
'''
value = [i for i in range(1, 6+1)]
print(value)

#4-6-2
'''
결과: [6,5,4,3,2,1]
'''
value2 = [i for i in reversed(range(1, 6+1))]
print(value2)

#4-6-3
'''
결과: [[1,2,3],[1,2,3],[1,2,3]]
'''
value = [ [i for i in range(1,4)] for x in range(3)]
print(value)

#4-6-4
'''
결과: [[1,2,3],[4,5,6],[7,8,9]]
'''
value4 = [[i for i in range(j*3+1, j*3+4)] for j in range(3)]
print(value4)

#or
value5 = [list (range(j*3+1, j*3+4)) for j in range(3)]
print(value5)

