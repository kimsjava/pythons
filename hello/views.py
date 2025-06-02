from django.shortcuts import render, redirect  # render, redirect 함수 import 추가
from .models import Friend
from .forms import HelloForm, FriendForm
from django.views.generic import DetailView
from django.views.generic import ListView

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


def delete(request, num):
    friend = Friend.objects.get(id=num)  # objects로 수정 (object → objects)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')  # /hello로 수정 ('hello' → '/hello')
    params = {
        'title': '데이터 삭제',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)


class FriendList(ListView):
    """친구 목록을 보여주는 클래스 기반 뷰"""
    model = Friend
    template_name = 'hello/friend_list.html'
    context_object_name = 'friends'  # 템플릿에서 {{friends}} 형태로 접근 가능

class FriendDetail(DetailView):
    """친구 상세 정보를 보여주는 클래스 기반 뷰"""
    model = Friend
    template_name = 'hello/friend_detail.html'
    context_object_name = 'friend'  # 템플릿에서 {{friend}} 형태로 접근 가능