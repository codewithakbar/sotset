"""
URL configuration for sotset project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from sotset.settings import DEBUG, STATIC_ROOT, STATIC_URL

from home import views as HomeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('chat/', include("messager.urls")),
    path('videolar/', include("video.urls")),
    path('tadbir/', include("events.urls")),
    path('gruppa/', include("gruppa.urls")),
    path('blog/', include("blog.urls")),

]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]