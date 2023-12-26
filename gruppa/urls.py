from django.urls import path
from .views import gruppa_page


urlpatterns = [
    path('', gruppa_page, name='gruppa'),
]
