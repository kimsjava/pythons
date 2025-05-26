from django.shortcuts import render  # render 함수 import 추가
from django.views.generic import TemplateView
from .models import Friend
from .forms import SessionForm
# Create your views here.

# 함수형 뷰
def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': 'all friends',
        'data': data,
    }
    print(f'params: {params}')
    return render(request, 'hello/index.html', params)

# HelloView 클래스 추가 (urls.py에서 사용한다면)
class HelloView(TemplateView):
    template_name = 'hello/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hello'
        context['message'] = 'all friends'
        context['data'] = Friend.objects.all()
        return context