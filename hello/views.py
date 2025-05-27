from django.shortcuts import render  # render 함수 import 추가
from .models import Friend
from .forms import HelloForm

# 함수형 뷰
def index(request):
    data = Friend.objects.all().values()
    params = {
        'title': 'Hello',
        'message': 'all friends',
        'form':HelloForm(),
        'data': data,
        
    }
    
    # if request.method == 'POST':
    #     num = request.POST['id']
    #     item = Friend.objects.get(id=num)
    #     params['data'] = [item]
    #     params['form'] = HelloForm(request.POST)
    # else:
    #     params['data'] = Friend.objects.all()
        
    return render(request, 'hello/index.html', params)