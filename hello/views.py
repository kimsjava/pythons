from django.shortcuts import render  # render 함수 import 추가
from .models import Friend
from .forms import HelloForm

def __new_str(friend):
    if friend is None:
        return ''
    return f"id={friend.id} | name={friend.name} | age={friend.age}"

# 함수형 뷰
def index(request):
    friendAll = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': friendAll,
    }
    return render(request, 'hello/index.html', params)