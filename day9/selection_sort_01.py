'''
0,1로만 이루어진 리스트(순서는 랜덤)를 정렬하세요. 
가능한 가장 빠른 방법을 찾아보세요
'''

from random import choice

raw = [0,1]
target = []

for _ in range(1000):
    target.append(choice(raw))

def solution(A):
    length = len(A)
    sum_1 = sum(A)
    string_value = '0' * (length - sum_1) + '1' * sum_1
    return list(map(int, list(string_value)))

print(solution(target))



