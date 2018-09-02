from django.shortcuts import render

# Create your views here.

def review(request, movie_id=None):
    return render(request, 'review.html')