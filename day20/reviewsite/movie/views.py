from django.shortcuts import render #, HttpResponse

import requests
from bs4 import BeautifulSoup as bs

from .models import SearchResult, Movie
# Create your views here.

def search_movie(request): #여기서 받은 request는 url에서 받은 것
    #크롤링해서 결과값을 찾고, 보여주는 곳
    if request.method == "POST": #받은게 있다면 크롤링해서 model에 저장
        keyword = request.POST['keyword']
        i = 1
        search_result = SearchResult.objects.create(
            keyword = keyword
        )
        while True:
            url = "http://www.cgv.co.kr/search/movie.aspx?query={}&page={}".format(keyword, i)
            response = requests.get(url)
            result = bs(response.text, 'html.parser')
            try: 
                ul = result.find('div', {'sect-chart'}).ul
                for li in ul.findAll("li"):
                    Movie.objects.create(
                        name = li.find('strong').text, 
                        img_url = li.img['src'], 
                        release_date = '-'.join(li.i.text.split('.')),
                        search_result = search_result
                    )
                i += 1
            except AttributeError:
                break
        

    #print(request.POST['keyword'])
    return render(request, 'search.html') #넘겨 받았던, 아니던, search.html 호출 
                                        #현재는 search.html에 넘겨줄 게 없기 때문에 매개 변수가 없는 것. 



