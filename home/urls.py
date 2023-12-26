from django.urls import path, re_path

from home import views as HomeViews


urlpatterns = [
    path('', HomeViews.homepage, name="home"),
]

