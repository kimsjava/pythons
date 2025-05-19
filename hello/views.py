from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    params = {
        'title': 'Hello/Index',
        'msg': 'これは、sample',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello/Form',
        'msg': f'konbanwa {msg} san',
    }
    return render(request, 'hello/index.html', params)

