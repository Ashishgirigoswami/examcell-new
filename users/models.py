from django.contrib.auth.models import AbstractUser,User
from django.db import models
from new_project import settings



class CustomUser(AbstractUser):

    first_name= models.CharField(max_length=30, blank=True)
    last_name =  models.CharField(max_length=30, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    Student_id=  models.IntegerField(null=False,primary_key=True,blank=True)
    #Department=models.ForeignKey(Department.department,on_delete=models.CASCADE)



class Employee(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eid     = models.CharField(max_length=20)
    ename   = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    USERNAME_FIELD = 'identifier'
    class Meta:
        db_table = "employee"
class Department(models.Model):
    department=models.CharField(max_length=10)
