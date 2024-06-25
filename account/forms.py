from django import forms
from users.models import User 
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    
class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        
        current_user = kwargs.get('instance', None)

        if current_user and current_user.username:
            self.fields['username'].widget.attrs['class'] = 'lg:w-1/2 w-full'
            self.fields['username'].widget.attrs['placeholder'] = current_user.username
            self.fields['first_name'].widget.attrs['placeholder'] = current_user.first_name
            self.fields['last_name'].widget.attrs['placeholder'] = current_user.last_name

            self.fields['email'].widget.attrs['placeholder'] = current_user.email
            # self.fields['avatar'].widget.attrs['class'] = "hidden"
            # self.fields['avatar'].widget.attrs['id'] = "file"
            # self.fields['avatar'].widget.attrs['type'] = "file"
            # self.fields['avatar'].widget.attrs['name'] = "avatar"


class UserAvatarUploadForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['avatar']

    def __init__(self, *args, **kwargs):
        super(UserAvatarUploadForm, self).__init__(*args, **kwargs)
        
        self.fields['avatar'].widget.attrs['class'] = "hidden"
        self.fields['avatar'].widget.attrs['id'] = "file"
        self.fields['avatar'].widget.attrs['type'] = "filess"
        self.fields['avatar'].widget.attrs['name'] = "avatar"


class UserBGAvatarUploadForm(forms.ModelForm):
    bg_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['bg_avatar']

    def __init__(self, *args, **kwargs):
        super(UserBGAvatarUploadForm, self).__init__(*args, **kwargs)
        
        self.fields['bg_avatar'].widget.attrs['class'] = "hidden"
        self.fields['bg_avatar'].widget.attrs['id'] = "createStatusUrl"
        self.fields['bg_avatar'].widget.attrs['type'] = "file"


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['placeholder'] = "Bu yerga o'z bioingizni yozing... "
        self.fields['bio'].widget.attrs['rows'] = 5
        self.fields['bio'].widget.attrs['class'] = "w-full"
        



