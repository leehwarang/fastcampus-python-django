'''
선택정렬: 내림차순으로 정렬
'''

from random import choice

raw_list = list(range(-50, 50+1))
#raw_list = [0, 1, 2, ..., 100]

target_list = []

for _ in range(100):
    target_list.append(choice(raw_list))
print(target_list) #정렬해야하는 리스트

def selection_sort_reverse(A):
    result = []

    while len(A) != 0: 
        max_num = A[0] #raw_list의 range가 변경될 수 있기 때문에, 절대적인 숫자를 대입하는 것은 좋지 않다. 
        for i in A:
            if max_num < i:
                max_num = i
        result.append(max_num) #모든 원소를 비교하여 가장 작은 값을 result에 append함. 
        A.remove(max_num)
    return result

print(selection_sort_reverse(target_list))
    



