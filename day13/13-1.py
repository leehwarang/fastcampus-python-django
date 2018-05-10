#ndArray 연산

import numpy as np

data = [[1,2,3], [4,5,6], [7,8,9]]
data = np.array(data) #ndArray로 생성

print(data)
print(data + 3) #각 요소에 3 더하기
print(data * 3) #각 요소에 3 곱하기
print(data ** 3) #각 요소에 3 제곱하기
print(data / 10) #각 요소에 10 나누기