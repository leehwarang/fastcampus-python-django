from multi import multi_all
from sum import add_1

import pprint
import random

print(__name__) #__main__출력

def main():
    print("메인 파일입니다.")

if __name__ == "__main__":
    main()
    print("내가 시작 포인트이다!")
    print(add_1(100))


#print(multi_all(1,2,3,4,5))
#print(add_1(100))

'''
import sys
sys.path
라고 하면 어떤 위치들이 뜨는데...그 장소에서 우리가 필요한 module을 불러올 수 있는 것. 
제일 처음에 있는 비어있는 string은 현재 경로(day6 디렉토리)를 의미하기 떄문에 day6에 있는 파일들을 모듈로써 불러올 수 있는 것. 
만약 del sys.path[0]하면 day6에 있는 파일을 모듈로써 불러올 수 없다. 
'''

'''
main.py / multi.py / sum.py 각각의 모듈에 print(__name__) 함수를 넣었다. 
만약 cmd에서 python3 main.py / python3 multi.py / python3 sum.py라고 했을 때는 모두 __main__이 출력 되었는데, 
python shell에서 각각의 모듈을 import 시켰을 때는 main / multi / sum 이라고 출력되었다. 

cmd에서 python3 main.py / python3 multi.py / python3 sum.py라고 한 것은 모듈을 호출한게 아니라, 단지 시작 파일로써 실행 시킨 것. 
'''



