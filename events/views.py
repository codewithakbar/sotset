from django.shortcuts import render



def event_page(request):

    return render(request, 'events/event.html')