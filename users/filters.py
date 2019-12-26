from django.contrib.auth.models import User
import django_filters
from .models import  CustomUser,Department,Course,AssignFaculty,marks_upload

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = [ 'first_name', 'last_name','Semester','department' ]

class departmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = [ 'Department_code','Department_name' ]

class courseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = [ 'course','Course_name','Course_code' ]
class assignedFilter(django_filters.FilterSet):
    class Meta:
        model = AssignFaculty
        fields = [ 'course_name' ]
class pdfFilter(django_filters.FilterSet):
    class Meta:
        model = marks_upload
        fields = [ 'subject_name' ]