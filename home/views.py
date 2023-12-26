from django.shortcuts import render

from home.models import Logo



def homepage(request):
    
    return render(request, "home/homepage.html", {"logo": Logo.objects.all()[:1]}) # logo base ichinda shunichin chiqmidi



