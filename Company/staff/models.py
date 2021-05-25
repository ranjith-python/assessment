from django.db import models

# Create your models here.


class Employee(models.Model):
    EmployeeName = models.CharField(max_length=255,null=True)
    Department = models.CharField(max_length=255,null=True)
    Email = models.EmailField(null=True)
    DateOfBirth = models.DateField(null=True)
    Picture = models.FileField(upload_to = 'employee/%Y/%m/%d/',blank=True,null=True)

class Department(models.Model):
    DepartmentName = models.CharField(max_length=255,null=True)
    Manager  = models.ForeignKey(Employee,null=True,on_delete=models.PROTECT,related_name='+')
