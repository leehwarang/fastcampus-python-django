from django.shortcuts import render, get_object_or_404, redirect

from movie.models import Movie
from .models import Review

# Create your views here.

def review(request, movie_id=None):
    movie = get_object_or_404(Movie, pk = movie_id)
    #POST인 경우(==사용자가 movie에 리뷰를 작성했을 때.)
    if request.method == "POST": 
        Review.objects.create(
            movie = movie, 
            title = request.POST.get('title'),
            content = request.POST.get('content')
        )
        return redirect('search')
    #POST가 아닌 경우에(==GET으로 받는 경우, 처음에 movie_id를 받을 때)
    result = {
        'movie': movie #movie_id를 가진 movie 객체를 딕셔너리에 저장함
    }
    return render(request, 'review.html', result) #해당 movie에 리뷰를 작성할 수 있는 html로 렌더링