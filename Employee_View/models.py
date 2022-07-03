from django.db import models


# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

class Role(models.Model):
    role = models.CharField(max_length=300)

    def __str__(self):
        return self.role

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()


