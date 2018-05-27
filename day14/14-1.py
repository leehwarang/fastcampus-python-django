import pandas as pd
from pandas import DataFrame
import numpy as np

data = [[24946, 25119, 25247, 25371, 25509],
        [12126, 12282, 12423, 12612, 12809],
        [9990, 9975, 9941, 9852, 9776],
        [3456, 3452, 3452, 3447, 3429],
        [3278, 3307, 3330, 3346, 3355],
        [2830, 2862, 2883, 2907, 2923],
        [2661, 2671, 2678, 2686, 2681],
        [2476, 2475, 2469, 2465, 2465],
        [2062, 2088, 2103, 2123, 2148],
        [1821, 1829, 1835, 1833, 1830],
        [1784, 1792, 1797, 1800, 1796],
        [1565, 1578, 1589, 1596, 1605],
        [1545, 1553, 1542, 1535, 1531],
        [1506, 1510, 1517, 1520, 1521], 
        [1504, 1510, 1517, 1520, 1521],
        [1137, 1151, 1164, 1169, 1166],
        [570, 583, 599, 619, 634],
        [118, 132, 187, 233, 276]
    ]

df = DataFrame(data, columns=['2013', '2014', '2015', '2016', '2017'], index=['수도권', '경기', '서울', '부산', '경남', '인천', '경북', '대구', '충남', '전북', '전남', '충북', '대전', '강원', '광주', '울산', '제주', '세종'])

print(df)

#1) 인수가 2017년 기준 3000명 이하인 지역을 출력하세요. 
print(df[df['2017'] <= 3000].index)

#2) 각 년도별로 인구수가 1000명 이하는 위험, 5000명 이하는 주의, 그 이상은 안정이라는 데이터를 가지도록 조작하세요. 

def substitution(x):
    if x <= 1000:
        return "위험"
    elif x <=5000:
        return "주의"
    else:
        return "안정"

custom_df = df.applymap(substitution)

print(custom_df)