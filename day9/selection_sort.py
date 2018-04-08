'''
선택정렬: 오름차순으로 정렬
빅오: O(n^2)
'''
from random import choice

raw_list = list(range(0, 100+1))
#raw_list = [0, 1, 2, ..., 100]

target_list = []

for _ in range(100):
    target_list.append(choice(raw_list))
print(target_list) #정렬해야하는 리스트

def selection_sort(A):
    result = []

    while len(A) != 0: 
        min_num = 100
        for i in A:
            if min_num > i:
                min_num = i
        result.append(min_num) #모든 원소를 비교하여 가장 작은 값을 result에 append함. 
        A.remove(min_num)
    return result

print(selection_sort(target_list))
    




