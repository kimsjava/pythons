from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
# Create your views here.


class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Hello',
            # 'message': 'you date',
            # 'd1':'',
            # 't1':'',
            # 'dt1':'',
            'form': HelloForm(),
            'result': None,
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        self.params['result'] = f'you selected:{request.POST.getlist("choice")}'
            
        self.params['form'] = HelloForm(request.POST)
        self.params['message'] = f'Hello {request.POST['name']}, your age is {request.POST['age']} and your mail {request.POST['mail']}'

        return render(request, 'hello/index.html', self.params)