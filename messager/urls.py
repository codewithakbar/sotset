from django.urls import path, re_path

from . import views as ChatViews


urlpatterns = [
    path('', ChatViews.chat_page, name="chat"),
]

