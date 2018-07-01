import datetime

from django.shortcuts import render, get_object_or_404 #HttpResponse
from .models import Post, Comment

def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list' : post_list}
    return render(request, 'index.html', context)
    # now_time = str(datetime.datetime.now())
    # name = request.GET.get('name')

    # if not name:
    #     name = '손님'
    # return HttpResponse(
    #     "<h1>Hi {}</h1>".format(name)+ '<br/><br/>' + now_time)

def post_detail(request, post_id):
    #post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id) #post_id가 있는 경우에는 보여주고, 없는 경우에는 404 error를 띄움
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comments' : comments
    }
    return render(request, 'post.html', context)
# Create your views here.
