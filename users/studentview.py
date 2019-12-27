from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render
#from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from .forms import CustomUserCreationForm,edit_studentprofile
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.core.mail import EmailMessage
from .models import Assignsubtosem,marks_upload
from .filters import subFilter
from django.contrib.auth import get_user_model,update_session_auth_hash

User = get_user_model()


def register(request):
    if request.POST:
        form= CustomUserCreationForm(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='student')
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
            group = Group.objects.get(name='faculty')
            user.groups.add(group)
            messages.success(request,f'Your account has been created,you can now login')
            return redirect('adminloginform')
    else:
        form = CustomUserCreationForm()
       # profileform=ProfileForm()
    return render(request, 'users/student_registration.html', {'form':form})



def user_log(request):
    user=request.user
    return user
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
                Session.user=request.user
                return HttpResponseRedirect('/student_home')
    return render(request, 'users/student login.html')

@login_required
def profile(request):
    return render(request,'users/studentprofile.html')

@login_required
def editstudentprofile(request):
    if request.method== 'POST':
        form = edit_studentprofile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('studentprofile')
    else:
        form = edit_studentprofile( instance=request.user)
        args={'form':form}
        return render(request,'users/editstudentprofile.html',args)
@login_required
def change_password(request):
    if request.method== 'POST':
        form= PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('studentprofile')
        else:
            return redirect('student_change_password')
    else:
        form= PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'users/change_password.html',args)

def password_reset(request):
    if request.method=='POST':
        form= PasswordResetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('password_reset_done')
    else:
        form= PasswordResetForm()
        args={'form':form}
        return render(request,'user/password_reset.html',args)

@login_required
def assigned_subjects(request):

    course_list = marks_upload.objects.filter(Semester= request.user.Semester)
    user_filter = subFilter(request.GET, queryset=course_list)
    return render(request, 'users/subject_marks.html', {'filter': user_filter})





