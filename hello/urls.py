from django.urls import path
from . import views  # 전체 모듈을 import

urlpatterns = [
    path('', views.index, name='index'),  # 함수형 뷰 사용
    # 기타 URL 패턴들...
]