from django.urls import path

from .views import search_movie

urlpatterns = [
    path('', search_movie, name="search"), #같은 url이지만 값을 받지 않는 경우
    path('<str:keyword>', search_movie, name="search-result"),#같은 url이지만 값을 받는 경우
]