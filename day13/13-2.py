#ndArray 타입 전환

import numpy as np

data = [[1,2,3], [4,5,6], [7,8,9]]
data = np.array(data) #ndArray로 생성

float_array = data.astype(np.float64) #float64로 타입 전환
print(float_array.dtype)
unicode_array = data.astype(np.unicode) #unicode로 타입 전환
print(unicode_array.dtype)
object_array = data.astype(np.object) #object로 타입 전환
print(object_array.dtype)