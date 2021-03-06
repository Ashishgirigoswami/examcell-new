from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render
#from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    if request.method=='POST':
        form= CustomUserCreationForm(request.POST)
        profileForm = ProfileForm(request.POST)
        if form.is_valid():

            user=form.save(commit=False)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='group_name')
            user.groups.add(group)
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('users/accountactivate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            #profileform.save()
            #username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created,you can now login')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
       # profileform=ProfileForm()
    return render(request, 'users/register.html', {'form':form})





from django.shortcuts import render

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home')
    return render(request, 'users/student login.html')

