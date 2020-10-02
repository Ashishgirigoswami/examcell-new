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
from .forms import CustomUserCreationForm,edit_adminprofile,Department_form,Course_from,AssignFacultyform,Assignsemform
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.shortcuts import render
from .filters import UserFilter,departmentFilter,courseFilter,assignedFilter
from .models  import Department,Course,AssignFaculty,Assignsubtosem

User = get_user_model()

@login_required
def profile(request):
    return render(request,'users/userprofile.html')

@login_required
def edit_profile(request):
    if request.method== 'POST':
        form= edit_adminprofile(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('adminprofile')
    else:
        form= edit_adminprofile(instance=request.user)
        args={'form':form}
        return render(request,'users/editadminprofile.html',args)


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
                return HttpResponseRedirect('/admin_home')
    return render(request, 'users/admin login.html')

@login_required
def change_password(request):
    if request.method== 'POST':
        form= PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('adminprofile')
        else:
            return redirect('change_password')
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
        return render(request,'users/password_reset.html',args)

@login_required
def studentsearch(request):
        user_list = User.objects.filter(groups__name='student')
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, 'users/student_list.html', {'filter': user_filter})

@login_required
def facultysearch(request):
        user_list = User.objects.filter(groups__name='faculty')
        print(type(user_list))
        user_filter = UserFilter(request.GET, queryset=user_list)
        print(type(user_filter))
        return render(request, 'users/faculty_list.html', {'filter': user_filter})


@login_required()
def add_department(request):
    department_list = Department.objects.all()
    user_filter = departmentFilter(request.GET, queryset=department_list)

    if request.method=='POST':
        form= Department_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Department')
    else:
        form= Department_form()
        args={'form':form,'filter': user_filter}
        return render(request,'users/add_department.html',args)


@login_required()
def add_course(request):
    course_list = Course.objects.all()
    user_filter = courseFilter(request.GET, queryset=course_list)
    if request.method=='POST':
        form= Course_from(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Course')
    else:
        form= Course_from()
        args={'form':form,'filter': user_filter}
        return render(request,'users/add_course.html',args)


@login_required()
def assign_Course(request):
    course_list = AssignFaculty.objects.all()
    user_filter = assignedFilter(request.GET, queryset=course_list)
    if request.method=='POST':
        form= AssignFacultyform(request.POST,)

        if form.is_valid():
            form.save()
            return redirect('assign_course')
        else:
         return HttpResponse('course is already assigned to faculty!!!!')
    else:
        form= AssignFacultyform()
        args={'form':form,'filter': user_filter}
        return render(request,'users/assign_course.html',args)

@login_required()
def assign_Semester(request):

    if request.method=='POST':
        form= Assignsemform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('assign_semester')
        else:
         return HttpResponse('course is already assigned to faculty!!!!')
    else:
        form= Assignsemform()
        args={'form':form,}
        return render(request,'users/assign_semester.html',args)




