from django.contrib import admin
from .models import Employee, Department, Role


# Register your models here.

class Department_admin(admin.ModelAdmin):

    list_display = ('id','department')


admin.site.register(Department, Department_admin)


class Employee_admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dept', 'salary', 'bonus', 'role', 'phone', 'hire_date')


admin.site.register(Employee, Employee_admin)


class Role_admin(admin.ModelAdmin):
    list_display = ('id','role')


admin.site.register(Role, Role_admin)
