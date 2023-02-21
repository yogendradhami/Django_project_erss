from django.shortcuts import render, redirect
from .forms import EmployeeCreateForm
from .models import Employee, User, Department

# Create your views here.
def employee_index(request):
    employee_list = Employee.objects.all()
    context = {"data": employee_list}
    return render(request, 'employees/index_employee.html', context) # error showing here

def employee_add(request):
    emp_create_form = EmployeeCreateForm()
    context = {"form": emp_create_form}

    if request.method == "POST":
        emp = Employee()
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))

        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST['address'] # [''] is same as above .get('') we can write by both method
        emp.blood_group = request.POST.get('blood_group')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.gender = request.POST.get('gender')
        emp.join_date = request.POST.get('join_date')
        emp.user = user
        emp.department= department
        emp.save()
        return redirect('emp-index')
    return render(request, 'employees/add_employee.html', context)

def employee_edit(request):
    return render(request, 'employees/edit_employee.html')

def employee_show(request):
    return render(request, 'employees/show.employee.html')