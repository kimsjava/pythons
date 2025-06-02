from django.shortcuts import render, redirect  # render, redirect 함수 import 추가
from .models import Friend
from .forms import HelloForm, FriendForm


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
        'form': FriendForm(),  # FriendForm 사용
    }
    # POST 요청 처리
    if request.method == 'POST':
        form = FriendForm(request.POST)  # FriendForm으로 변경
        if form.is_valid():
            # ModelForm은 save() 메서드로 모델 인스턴스를 직접 생성하고 저장할 수 있음
            form.save()
            return redirect(to='/hello')
        else:
            params['form'] = form
    return render(request, 'hello/create.html', params)




def edit(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == 'POST':
        friend = FriendForm(request.POST, instance=obj)  # FriendForm 사용
        if friend.is_valid():
            friend.save()
            return redirect(to='/hello')
        
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),  # FriendForm 사용
    }
    return render(request, 'hello/edit.html', params)