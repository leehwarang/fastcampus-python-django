'''
모듈(module): 프로그램(기능)의 모음
모듈을 불러오는 방식
1) from ** import ** 
2) import **

우리가 방금 만든 파일을 모듈로써 불러오기
ex1) from file import add_all -> python shell에서 add_all(1,2,3,4,5) 바로 사용 
ex2) import file -> python shell에서 file.add_all(1,2,3,4,5) 사용 
'''

def add_all(*args):
    return sum(args)



