import requests
from bs4 import BeautifulSoup as bs

country_dic = {
    '1': '2', 
    '2': '252',
    '3': '228', 
    '4': '69'
}

user_select = input("원하는 국가를 선택하세요. 1)가봉 2)필리핀 3)터키 4)미국")
base_url = "http://www.0404.go.kr/m/dev/country_view.do?idx="

if user_select == '1':
    full_url = base_url + country_dic['1']
elif user_select == '2': 
    full_url = base_url + country_dic['2']
elif user_select == '3':
    full_url = base_url + country_dic['3']
else:
    full_url = base_url + country_dic['4']

response = requests.get(full_url)
result = bs(response.text, 'html.parser')
a = result.find('div', {'class':'map_box'})
b = a.find('img')
c = b.get("src")
page_url = "http://www.0404.go.kr/"
print(page_url+c)


    
    

