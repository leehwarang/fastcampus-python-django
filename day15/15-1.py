'''
온도 변화 그래프 그리기
2018년 1월 실제 하루 최저, 최고 온도 그래프를 그리세요.
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series

x_range = np.arange(1, 32, 1)
minumum_tp = Series([-5.1, -4.3, -7.1, -8.7, -5.6, -6.8, -5.7, -1.2, -6.1, -10.3, -13.6, -15.3, -6.6, -4.4, 1.8, 0.1, 2.4, -0.3, -2.5, -1.0, -3.7, -5.3, -14.6, -16.3, -16.4, -17.8, -15.9, -9.3, -11.6, -11.4, -5.2])
maximum_tp = Series([3.8, 1.8, -0.4, -0.7, 1.6, 2.9, 2.8, 4.0, -1.2, -4.8, -7.4, -5.4, -1.2, 5.4, 7.7, 6.8, 8.7, 4.5, 5.5, 6.9, 5.5, 4.0, -5.3, -10.7, -9.5, -10.7, -3.5, -1.2, -4.7, -0.8, 0])

plt.plot(x_range, minumum_tp, 'b-', x_range, maximum_tp, 'r--')
plt.xlabel('day')
plt.ylabel('temperature')
plt.title("January'temperature")


