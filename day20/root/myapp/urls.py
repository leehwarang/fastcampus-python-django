from django.urls import path
from . import views 

urlpatterns = [
    path("", views.post_list),
    path("<int:post_id>", views.post_detail, name="detail") #가변적인 값(post_id)을 받아서 함수(post_detail)에 넘기겠다는 의미
]