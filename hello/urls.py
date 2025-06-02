from django.urls import path
from . import views
from .views import FriendList
from .views import FriendDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    
    path('list/', FriendList.as_view(), name='friend_list'),
    path('detail/<int:pk>/', FriendDetail.as_view(), name='friend_detail'),
]