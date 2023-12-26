from django.shortcuts import render



def video_page(request):

    return render(request, "video/video.html")