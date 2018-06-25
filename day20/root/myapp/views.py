import datetime

from django.shortcuts import render, HttpResponse

def say_hi(request):
    now_time = str(datetime.datetime.now())
    name = request.GET.get('name')

    if not name:
        name = '손님'
    return HttpResponse(
        "<h1>Hi {}</h1>".format(name)+ '<br/><br/>' + now_time)

# Create your views here.
