from django.shortcuts import render, redirect  # render, redirect 함수 import 추가
from .models import Friend
from .forms import HelloForm


# 함수형 뷰
def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

# create model

def create(request):
    params = {
        'title': 'Create',
        'form': HelloForm(),
    }
    # POST 요청 처리
    if request.method == 'POST':
        form = HelloForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            birthday = form.cleaned_data.get('birthday')
            friend = Friend(
                name=name,
                mail=mail,
                gender=gender,
                age=age,
                birthday=birthday)
            friend.save()
            return redirect(to='/hello')
        else:
            params['form'] = form
    return render(request, 'hello/create.html', params)




