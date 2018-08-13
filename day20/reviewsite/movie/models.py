from django.db import models

# Create your models here.

#하나의 키워드를 검색했을 때 나오는 여러개의 결과(영화)를 Movie class에 저장할 것임
#같은 키워드를 검색했을 때, 하루 이내에 검색했으면 다시 크롤링 시도하지 않고, 저장한 데이터만 가지고 온다.

class SearchResult(models.Model):
    keyword = models.CharField(max_length = 50)
    search_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        #'어벤져스(2018.05.01'
        return '{}({})'.format(self.keyword, self.search_date)
        
class Movie(models.Model):
    name = models.CharField(max_length = 50)
    img_url = models.URLField() # == CharField(max_length=200)
    release_date = models.DateField()
    search_result = models.ForeignKey(
        SearchResult,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return '{}({})'.format(self.name, self.release_date)