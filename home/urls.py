from django.urls import path, re_path

from home import views as HomeViews

app_name = "home"

urlpatterns = [
    path('', HomeViews.homepage, name="home"),
]

