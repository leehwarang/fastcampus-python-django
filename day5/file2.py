#함수의 이름도 곧 변수이다. 

likes = []

def input_like():
    like = input("좋아하는 걸 하나 입력하세요.")
    likes.append(like)
    print(likes)

input_like()
input_like()
input_like()
