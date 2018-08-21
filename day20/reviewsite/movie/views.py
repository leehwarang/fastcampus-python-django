from django.shortcuts import render, redirect #, HttpResponse
from django.utils import timezone 
import requests
from bs4 import BeautifulSoup as bs

from .models import SearchResult, Movie
# Create your views here.

def search_movie(request, keyword=None): #여기서 받은 request는 url에서 받은 것
    #크롤링해서 결과값을 찾고, 보여주는 곳
    print(keyword)
    if request.method == "POST": #받은게 있다면 크롤링해서 model에 저장
        keyword = request.POST['keyword']
        if not keyword:
            return redirect('search')
        results = SearchResult.objects.filter(keyword=keyword).order_by('-search_date') #가장 최근에 검색한 것 부터 보여주기 위해서 search_date의 역순 정렬
        if results: #검색한 데이터가 있고
            recent = results[0] #가장 최근에 검색한 데이터
            if recent.search_date - timezone.now() < timezone.timedelta(days = 1): #검색한지 하루가 안된 경우
                print("검색한지 하루가 지나지 않았습니다.")
                return redirect('search-result', keyword=keyword)
        i = 1
        search_result = SearchResult.objects.create(
            keyword = keyword
        )
        while True:
            print("크롤링 시작")
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
        return redirect('search-result', keyword=keyword)

    #GET메소드 redirect된 경우, keyword가 있는 경우
    if keyword:
        result = SearchResult.objects.filter(keyword=keyword).order_by('-search_date')
        if result[0].movie_set.all():
            return render(request, 'search.html', {'result': result[0]})
        else: 
            return render(request, 'search.html', {'result': False})

    #GET메소드 ->그냥 html 파일로 렌더링 시키기 
    #print(request.POST['keyword'])
    return render(request, 'search.html') #넘겨 받았던, 아니던, search.html 호출 
                                        #현재는 search.html에 넘겨줄 게 없기 때문에 매개 변수가 없는 것. 



