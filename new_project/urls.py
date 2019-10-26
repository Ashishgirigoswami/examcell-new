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
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from users import  adminview as av,studentview as sv,facultyview as fv,views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='index.html'), name='base'),
    path('aboutus/', TemplateView.as_view(template_name='about.html'), name='aboutus'),
    path('register/',v.register, name='register'),
    path('Dashboard/',v.Dashboard, name='Dashboard'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    path('admin login/', av.login_user, name='adminloginform'),
    path('student login/', sv.login_user, name='studentloginform'),
    path('faculty login/', fv.login_user, name='facultyloginform'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # new0
]


