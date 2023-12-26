from django.urls import path, re_path

from . import views as VideoViews


urlpatterns = [
    path('', VideoViews.video_page, name="video"),
]

