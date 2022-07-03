from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee,Role,Department


# Create your views here.
def Home_page(request):
    return render(request, 'Employee_View/Home_Page.html')

def Add_Page(request):
    if request.method == 'POST':
        # Gettng the form details
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])

        # Typecasting depoartment to int
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        hire_date = request.POST['hire_date']

        # in user dept_id means Go to Department Table and get the row by id and fill the details in EMployees table in dept column
        # Same Goes with role
        user = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=department,role_id = role,phone=phone,hire_date=hire_date)
        user.save()
        return redirect('All_Page')
    else:
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'Employee_View/Add.html',
                      {
                          'dept':departments,
                          'role':roles
                      })

def Remove_Page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        deleting_Employee = Employee.objects.get(first_name=first_name,last_name=last_name)
        deleting_Employee.delete()

        return redirect('All_Page')
    else:
        return render(request, 'Employee_View/Remove.html')

def Filter_Page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        filteringing_Employee = Employee.objects.get(first_name=first_name,last_name=last_name)


        return render(request, 'Employee_View/Filter_result.html',{
            'filter':filteringing_Employee
        })
    else:

        return render(request, 'Employee_View/Filter.html')

def All_Page(request):
    Details = Employee.objects.all()

    return render(request, 'Employee_View/View_All.html',{
        'pass':Details
    })
