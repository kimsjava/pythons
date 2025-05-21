from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import SessionForm
# Create your views here.
class HelloView(TemplateView):
    
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'form': SessionForm(),
            'result': None,
        }

    def get(self, request):
        self.params['result'] = request.session.get('last_msg', 'no message')
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        ses = request.POST.get('session', '')
        self.params['result'] = f'sned: {ses}.'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)
        
        return render(request, 'hello/index.html', self.params)
    
    
    def sample_middleware(self, get_response):
        
        def middleware(request):
            print(f'request: {request}')
            return get_response(request)
        
        return middleware