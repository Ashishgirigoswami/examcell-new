
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Course,Department,AssignFaculty,marks_upload,Semester,Assignsubtosem
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
CustomUser = get_user_model()

Gender_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ]

Department_CHOICES= [
    ('first year','first year'),
    ('cs', 'computer science'),
    ('me', 'mechanical'),
    ('ee', 'electrical'),
    ('ec', 'elctronics'),
    ('ce', 'civil'),
]
Semester_CHOICES= [
    ('first', 'first '),
    ('second', 'second'),
    ('third', 'third'),
    ('forth', 'forth'),
    ('fifth', 'fifth'),
    ('sixth', 'sixth '),
    ('seveth', 'seveth'),
    ('eight', 'last'),
]



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder':'Enter username'}))
    email = forms.EmailField(max_length=30,widget=forms.TextInput
            (attrs={'class':'input100','placeholder':'Enter email'}))
    password1 = forms.CharField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder': 'Enter password','type':'password'}))
    password2 = forms.CharField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder': 'Enter password','type':'password'}))
    first_name =forms.CharField(max_length=30,widget=forms.TextInput(
        attrs={'class':'input100','placeholder':'enter First name'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(
        attrs={'class':'input100','placeholder':'enter Last name'}))
    Student_id = forms.CharField(max_length=8,widget=forms.TextInput(
        attrs={'class':'input100','placeholder':'enter student id'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    Semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    gender = forms.CharField(max_length=8,widget=forms.Select(choices=Gender_CHOICES))
    mobile_no = forms.CharField(max_length=10,widget=forms.TextInput(
        attrs={'class':'input100','placeholder':'enter mobile no'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','first_name','last_name','mobile_no','Student_id','Semester','department')



class edit_adminprofile(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name','last_name','mobile_no','password')

class edit_studentprofile(UserChangeForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    Semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'mobile_no','Student_id','Semester','department',)
class edit_faculty_profile(UserChangeForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    Semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'mobile_no','department','password')

class teachercreationform(UserCreationForm):

    username = forms.CharField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder': 'Enter username'}))
    email = forms.EmailField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder': 'Enter password', 'type': 'password'}))
    password2 = forms.CharField(max_length=30, widget=forms.TextInput
    (attrs={'class': 'input100', 'placeholder': 'Enter password', 'type': 'password'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'enter First name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'enter Last name'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    gender = forms.CharField(max_length=8, widget=forms.Select(choices=Gender_CHOICES))
    mobile_no = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'enter mobile no'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'mobile_no','department')

    def clean_username(self):
        user= self.cleaned_data['username']
        try:
            match= CustomUser.object.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username already exist')
    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            mt= validate_email(email)
        except:
            return forms.ValidationError("email is not in correct format")
        return email
    def clean_confirm_password(self):
        pas= self.cleaned_data['password1']
        cpas=self.cleaned_data['password2']
        MIN_LENGTH=8
        if pas and cpas:
            if pas!=cpas:
                raise forms.ValidationError("password and confirm password are not matched")
            else:
                if len(pas)<MIN_LENGTH:
                    raise forms.ValidationError("password should have atleast of %d  letters",MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError("password should contains alphabates")

class Course_from(forms.ModelForm):
    course = forms.CharField(max_length=20,)
    Course_name = forms.CharField(max_length=30)
    Course_code = forms.CharField(max_length=15,)

    class Meta():
        model = Course
        fields = ('course','Course_name','Course_code')


class Department_form(forms.ModelForm):
    Department_name = forms.CharField(max_length=20,)

    Department_code = forms.CharField(max_length=15,)

    class Meta():
        model = Department
        fields = ('Department_name', 'Department_code')

class AssignFacultyform(forms.ModelForm):
    faculty=forms.ModelChoiceField(queryset=CustomUser.objects.filter(groups__name='faculty'))
    course_name=forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta():
        model = AssignFaculty
        fields = ('faculty', 'course_name')


class marksupload(forms.ModelForm):

    class Meta():
        model= marks_upload
        fields=('subject_name','pdf')

class Assignsemform(forms.ModelForm):
    Semester = forms.ModelChoiceField(queryset=Semester.objects.all())
    course_name = forms.ModelChoiceField(queryset=Course.objects.all())
    Department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta():
        model = Assignsubtosem
        fields = ('Semester','Department', 'course_name')




