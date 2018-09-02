from django.conf.urls import url
from django.contrib import admin

from photos.views import hello  #views에 있는 hello 함수 객체를 가지고 옴


urlpatterns = [
    url(r'^hello/$', hello),  # 이 줄도 추가합니다.
    url(r'^admin/', admin.site.urls),
]