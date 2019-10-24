
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Employee
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','first_name','last_name','Student_id','date_of_birth',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ()

class ProfileForm(CustomUserCreationForm):
    class Meta:
        model = Employee
        fields = ('eid', 'ename','econtact')