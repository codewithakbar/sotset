from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import LoginForm, UserAvatarUploadForm, UserBGAvatarUploadForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
            
    return render(request, 'account/login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@login_required
def acc_settings(request):
    return render(request, 'account/settings.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    try:
        profile_instance = request.user.profile
    except Profile.DoesNotExist:
        profile_instance = Profile(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        profile_form = ProfileEditForm(instance=profile_instance, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()            
            profile_form.save()
            messages.success(request, 'Profil muvaffaqiyatli yangilandi')
        else:
            messages.error(request, 'Xatolik, profil1 yangilanishida')

    elif request.method == "PUT":
        user_form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        profile_form = ProfileEditForm(instance=profile_instance, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()            
            profile_form.save()
            messages.success(request, 'Profil muvaffaqiyatli yangilandi')
        else:
            messages.error(request, 'Xatolik, profil1 yangilanishida')
            
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile_instance)

    return render(request, 'account/settings.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
@require_http_methods(["PUT"])
def upload_avatar(request):
    if request.method == 'PUT':
        user_avatar_form = UserAvatarUploadForm(instance=request.user, data=request.POST, files=request.FILES)

        if user_avatar_form.is_valid():
            user_avatar_form.save()
            messages.success(request, 'Avatar muvaffaqiyatli yangilandi')
        else:
            messages.error(request, 'Xatolik, avatar yangilanishida')
    else:
        user_avatar_form = UserAvatarUploadForm(instance=request.user)
    
    return render(request, 'account/settings.html', {'avatar_form': user_avatar_form})



@login_required
def user_profile(request):
    if request.method == 'POST':
        user_avatar_form = UserBGAvatarUploadForm(instance=request.user, data=request.POST, files=request.FILES)

        if user_avatar_form.is_valid():
            user_avatar_form.save()
            messages.success(request, 'Avatar muvaffaqiyatli yangilandi')
        else:
            messages.error(request, 'Xatolik, avatar yangilanishida')
    else:
        user_avatar_form = UserBGAvatarUploadForm(instance=request.user)

    return render(request, "account/profile.html", {'bg_avatar_form': user_avatar_form})

@login_required
def user_settings(request):
    if request.method == 'POST':
        user_avatar_form = UserAvatarUploadForm(instance=request.user, data=request.POST, files=request.FILES)

        if user_avatar_form.is_valid():
            user_avatar_form.save()
            messages.success(request, 'Avatar muvaffaqiyatli yangilandi')
        else:
            messages.error(request, 'Xatolik, avatar yangilanishida')
    else:
        user_avatar_form = UserAvatarUploadForm(instance=request.user)

    return render(request, "account/settings.html", {'bg_avatar_form': user_avatar_form})

