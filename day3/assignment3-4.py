'''
#3-4. Palindrome
앞에서 부터 읽어도, 뒤에서 부터 읽어도 같은 문자를 Palindrome, 즉 회문이라고 합니다. 
다음 문자들이 회문인지 아닌지 판별하는 코드를 작성해보세요. 
1) Anna
2) Radar
3) Step on no Pets
4) No lemon, no melon
'''

import re

print("문자를 입력해보세요.")
palindrome = input()

palindrome = re.sub("[-=.,#/?!:&]", "", palindrome) #특수 문자 제거
palindrome = palindrome.lower().strip().replace(" ","") #대소문자 무시, 공백 삭제, 띄어쓰기 무시 

answer = True

reverse = ''
j = -1 

for i in palindrome:
    reverse = i + reverse
    if palindrome[j:] == reverse:
        #print(palindrome[j:])
        #print(reverse)
        j = j-1 
    else: 
        answer = False
        break

if answer == True:
    print("회문 입니다.")
else:
     print("회문이 아닙니다.")