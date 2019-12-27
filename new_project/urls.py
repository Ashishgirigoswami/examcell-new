"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""examcell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetCompleteView,PasswordResetDoneView,PasswordResetConfirmView
from users import  adminview as av,studentview as sv,facultyview as fv,views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^Studentsearch/$',av.studentsearch, name='Student_search'),
    url(r'^Facultysearch/$',av.facultysearch, name='Faculty_search'),
    url(r'^course/$',av.add_course, name='Course'),
    url(r'^department/$',av.add_department, name='Department'),
    path('assign_course/',av.assign_Course, name='assign_course'),
    path('marks_upload/',fv.marks_Upload,name='marks_upload'),
    path('marks_pdf/',fv.assigned_pdf,name='marks_pdf'),
    path('Subjects/',sv.assigned_subjects,name='subjects'),
    path('assign_sem/',av.assign_Semester, name='assign_semester'),
    path('assigned_subject/',fv.assigned_subject, name='assigned_subject'),
    path('users/', include('django.contrib.auth.urls')),
    path('admin_home', TemplateView.as_view(template_name='admin_home.html'), name='adminhome'),
    path('student_home', TemplateView.as_view(template_name='student_home.html'), name='stundentyhome'),
    path('faculty_home', TemplateView.as_view(template_name='faculty_home.html'), name='facultyhome'),
    path('', TemplateView.as_view(template_name='index.html'), name='base'),
    path('aboutus/', TemplateView.as_view(template_name='about.html'), name='aboutus'),
    path('student_registration/',sv.register, name='studentregister'),
    path('teacher_registration/',fv.register, name='teacherregister'),
    path('adminprofile/',av.profile, name='adminprofile'),
    path('studentprofile/',sv.profile, name='studentprofile'),
    path('facultyprofile/',fv.profile, name='facultyprofile'),
    path('editadminprofile/',av.edit_profile, name='editadminprofile'),
    path('change_password/',av.change_password, name='change_password'),
    path('student_change_password/',sv.change_password, name='student_change_password'),
    path('faculty_change_password/',fv.change_password, name='faculty_change_password'),
    path('editstudentprofile/',sv.editstudentprofile, name='editstudentprofile'),
    path('password_reset',PasswordResetView.as_view(template_name='password_reset_form.html'),name="password_reset"),
    path('reset_password/done',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-'
         '[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),name='password_reset_confirm'),
    path('password_reset/complete',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    path('editfacultyprofile/',fv.edit_facultyprofile, name='editfacultyprofile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    path('admin login/', av.login_user, name='adminloginform'),
    path('student login/', sv.login_user, name='studentloginform'),
    path('faculty login/', fv.login_user, name='facultyloginform'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
    # new0
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


