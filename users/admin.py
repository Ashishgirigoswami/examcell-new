
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser,Course,Department,AssignFaculty,marks_upload,Semester,Assignsubtosem


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['email','username']




admin.site.register(CustomUser,CustomUserAdmin,)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(AssignFaculty)
admin.site.register(marks_upload)

admin.site.register(Semester)
admin.site.register(Assignsubtosem)
