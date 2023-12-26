from django.urls import path
from .views import post_detail, post_list

urlpatterns = [
    path('', post_list, name='blog'),
    path('<int:id>/', post_detail, name='post_detail'),
]
