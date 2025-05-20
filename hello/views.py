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
        selected_choices = request.POST.getlist("choice")  # 리스트로 가져오기
        selected_labels = []

        # 값만 출력할 경우
        for val in selected_choices:
            selected_labels.append(val)  # 'one', 'two' 등

        # 폼 재생성
        self.params['form'] = HelloForm(request.POST)

        # 텍스트로 출력
        self.params['result'] = "You selected: " + ", ".join(selected_labels)

        # 기타 필드 값 처리
        name = request.POST.get("name", "")
        age = request.POST.get("age", "")
        mail = request.POST.get("mail", "")
        self.params['message'] = f'Hello {name}, your age is {age} and your mail {mail}'

        return render(request, 'hello/index.html', self.params)