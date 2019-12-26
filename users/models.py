from django.contrib.auth.models import AbstractUser,User
from django.db import models
from new_project import settings


class Department(models.Model):
    Department_name=models.CharField(max_length=20,blank=True )
    Department_code=models.CharField(max_length=6,blank=True)
    class Meta:
         db_table="Department"

    def __str__(self):
        return self.Department_name

class Semester(models.Model):
    Semester=models.CharField(max_length=20,blank=True )
    type=models.CharField(max_length=6,blank=True)
    class Meta:
         db_table="Semester"

    def __str__(self):
        return self.Semester

class CustomUser(AbstractUser):

    first_name= models.CharField(max_length=30, blank=True)
    last_name =  models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100,blank=True)
    Student_id=models.CharField(max_length=8,blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    Semester=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=8,blank=True)
    mobile_no=models.CharField(max_length=10,blank=True)


class Course(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course    = models.CharField(max_length=20,blank=True)
    Course_name  = models.CharField(max_length=30,blank=True)
    Course_code = models.CharField(max_length=15,blank=True)
    class Meta:
        db_table = "Student"
    def __str__(self):
        return self.course


class AssignFaculty(models.Model):
    faculty=models.ForeignKey(CustomUser,on_delete=models.CASCADE, )
    course_name=models.OneToOneField(Course,on_delete=models.CASCADE,)
    class Meta:
         db_table="AssignFaculty"

    def __str__(self):
        return self.course_name.course

class Assignsubtosem(models.Model):
    Semester=models.ForeignKey(Semester,on_delete=models.CASCADE, )
    course_name=models.OneToOneField(Course,on_delete=models.CASCADE,)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,)
    class Meta:
         db_table="Assignsemester"

    def __str__(self):
        return self.Semester.Semester



class marks_upload(models.Model):
    subject_name= models.OneToOneField(AssignFaculty,on_delete=models.CASCADE)
    pdf=models.FileField(upload_to='documents/')





