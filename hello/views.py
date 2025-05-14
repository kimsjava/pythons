from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    
    if 'msg' not in request.GET:
        msg = request.GET['msg']
        result = 'you typed: "%s"' % msg
        msg = 'Hello, world!'
    else:
        result = 'please send msg parameter!'   
        
    return HttpResponse(result)
