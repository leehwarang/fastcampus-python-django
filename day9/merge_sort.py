from random import choice

raw = list(range(-50, 50+1))

target = []
for _ in range(100):
    target.append(choice(raw))

#print(target)

def _merge(A, B):
    result = []
    length = len(A) + len(B)
    for _ in range(length):
        try:
            if A[0] > B[0]:
                result.append(B[0])
                B.remove(B[0])
            else:
                result.append(A[0])
                A.remove(A[0])
        except IndexError:
            if len(A):
                result += A
                break
            else: 
                result += B
    return result 

def merge_sort(A):
    if len(A) < 2:
        return A
    left_list = merge_sort(A[:len(A)//2])
    right_list = merge_sort(A[len(A)//2:])
    return _merge(left_list, right_list)

print(merge_sort(target))