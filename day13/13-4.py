#ndArray boolean slice

import numpy as np

#1.홀수인 숫자는 0으로 바꾸기
data = [[1,2,3], [4,5,6], [7,8,9]]
data = np.array(data) #ndArray로 생성

data[data%2 != 0] = 0
print(data)

#2.5보다 큰 숫자는 10으로 바꾸기
data = [[1,2,3], [4,5,6], [7,8,9]]
data = np.array(data) #ndArray로 생성

data[data>5] = 0
print(data)

#3.제곱했을 때 홀수인 숫자만 남기고 0으로 바꾸기
data = [[1,2,3], [4,5,6], [7,8,9]]
data = np.array(data) #ndArray로 생성

data[(data ** 2) %2 == 0] = 0
print(data)
