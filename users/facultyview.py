from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.shortcuts import render
#from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from .tokens import account_activation_token
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from .forms import teachercreationform,edit_faculty_profile,marksupload
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model,update_session_auth_hash
from .models import AssignFaculty,marks_upload
from .filters import assignedFilter,pdfFilter

User = get_user_model()

def register(request):
    if request.method=='POST':
        form= teachercreationform(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='faculty')
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
            return redirect('facultyloginform')
    else:
        form = teachercreationform()

    return render(request, 'users/teacher_registration.html', {'form':form})





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
                request.session['user']=username
                login(request, user)
                return HttpResponseRedirect('/faculty_home')
    return render(request, 'users/faculty login.html')

@login_required
def profile(request):
    return render(request,'users/facultyprofile.html')

@login_required
def edit_facultyprofile(request):
    if request.method== 'POST':
        form= edit_faculty_profile(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('facultyprofile')
    else:
        form= edit_faculty_profile(instance=request.user)
        args={'form':form}
        return render(request,'users/editfacultyprofile.html',args)

def change_password(request):
    if request.method== 'POST':
        form= PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('facultyprofile')
        else:
            return redirect('faculty_change_password')
    else:
        form= PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'users/faculty_change_password.html',args)

def password_reset(request):
    if request.method=='POST':
        form= PasswordResetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('password_reset_done')
    else:
        form= PasswordResetForm()
        args={'form':form}
        return render(request,'users/password_reset.html',args)

@login_required
def assigned_subject(request):

    course_list = AssignFaculty.objects.filter(faculty=request.user)
    user_filter = assignedFilter(request.GET, queryset=course_list)
    return render(request, 'users/Assigned_subject.html', {'filter': user_filter})

@login_required
def marks_Upload(request):

    if request.method=='POST':
        form= marksupload(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('facultyhome')
        else:
            return redirect('marks_upload')
    else:
        form= marksupload()
    return render(request, 'marks_upload.html', {'form': form,})
@login_required
def assigned_pdf(request):

    course_list = marks_upload.objects.all()
    user_filter = pdfFilter(request.GET, queryset=course_list)
    return render(request, 'users/subject_marks.html', {'filter': user_filter})



