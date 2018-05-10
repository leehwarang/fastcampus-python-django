#ndArray 인덱스/슬라이스

import numpy as np

data = [[1,2,3], [4,5,6], [7,8,9]]
data = np.array(data) #ndArray로 생성

print(data[1,2]) #6 출력
print(data[1,1]) #5 출력

print(data[:2, :2]) #[[1,2],[4,5]] 출력
print(data[:3, 1:])#[[2,3],[5,6],[8,9]] 출력

