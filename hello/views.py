from django.shortcuts import render
from django.http import HttpResponse

from hello.form import HelloForm
# Create your views here.


def index(request):
    params = {
        'title': 'Hello',
        'msg': 'your date',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        params['message'] = f"名前:{request.POST['name']}\nメール:{request.POST['mail']}\n年齢:{request.POST['age']}"
        params['form'] = HelloForm(request.POST)
        
    return render(request, 'hello/index.html', params)
