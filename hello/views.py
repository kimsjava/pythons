from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request, id, nickname):
    result = f'you id: "{id}", your nickname: "{nickname}"'
    return HttpResponse(result)
