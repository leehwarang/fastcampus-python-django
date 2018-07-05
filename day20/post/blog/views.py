from django.shortcuts import render, redirect

# Create your views here.
from .models import Post

def post(request):
    #print(request.POST) #값을 넘겨 받음. 지정한 이름은 key, 입력받은 것을 value로 하는 딕셔너리 형태를 만들어줌
    if request.method == 'POST':
        #DB값 추가
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post') #DB에 값이 들어온 후 다시 보여주는 페이지를 post로 함
    else: #request.method == 'GET'일 때. (아무것도 전달 받은 것이 없을 때)
        posts = Post.objects.all()
        return render(
            request, 
            'post/post_list.html',
            {'posts': posts}
        )
