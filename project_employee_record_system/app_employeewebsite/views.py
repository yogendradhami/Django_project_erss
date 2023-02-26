from django.shortcuts import render, redirect
from .forms import EmployeeCreateForm
from .forms import DepartmentCreateForm
from .forms import SalaryCreateForm
from .models import Employee, User,Employee, Department, EmployeeSalary
from django.contrib import messages

# Create your views here.

# functions for employee section starts here

def employee_index(request):
    """Returns list of employee as context"""

    employee_list = Employee.objects.all()
    context = {"data": employee_list}
    
    return render(request, 'employees/index_employee.html', context)
 

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

        messages.success(request, 'Employee added successfully')

        return redirect('emp-index')

    return render(request, 'employees/add_employee.html', context)

def employee_edit(request, id):
    data = Employee.objects.get(id=id)
    department = Department.objects.all()
    user = User.objects.all()
    context = {"data": data, "department":department, "user":user}
    return render(request, 'employees/edit_employee.html', context)

def employee_update(request):
    if request.method == "POST":
       
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))
        emp= Employee.objects.get(id = request.POST.get('id'))
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

        messages.success(request, 'Employee details updated successfully')

        return redirect('emp-index')
   
def employee_show(request, id):
    data = Employee.objects.get(id=id)
    context = {"data":data}
    return render(request, 'employees/show_employee.html', context)

def employee_delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()

    messages.success(request, 'Employee deleted successfully')

    return redirect("emp-index")

# funtions for employee section ends here

# funtions for department section starts here

def department_index(request):
    department_list = Department.objects.all()
    context ={"data":department_list}
   
    return render(request, 'departments/index_department.html', context)

def department_add(request):
    dprt_create_form= DepartmentCreateForm()
    context = {"form":dprt_create_form}

    if request.method == "POST":
       dprt = Department()
       dprt.department_name = request.POST.get('department_name')
       dprt.short_name = request.POST.get('short_name')
       dprt.save()

       messages.success(request, 'Department added successfully')
       
       return redirect('dprt-index')
    return render(request, 'departments/add_department.html', context)

def department_edit(request,id):
    data = Department.objects.get(id=id)
    department = Department.objects.all()
    user =User.objects.all()
    context = {"data":data, "department":department, "user":user}
    return render(request, 'departments/edit_department.html', context)

def department_update(request):
    if request.method == "POST":

        dprt= Department.objects.get(id = request.POST.get('id'))
        dprt.department_name = request.POST.get('department_name')
        dprt.short_name = request.POST.get('short_name')
        dprt.save()

        messages.success(request, 'Department details updated successfully')

        return redirect('dprt-index')

def department_delete(request,id):
    data = Department.objects.get(id=id)
    data.delete()
    messages.success(request, 'Department deleted successfully')

    return redirect('dprt-index')

def department_show(request, id):
    data = Department.objects.get(id=id)
    context = {"data":data}
    return render(request, 'departments/show_department.html', context)

# function for department ends here


# funtions for salary section starts here

def salary_index(request):
    """ Return list of salary as context """

    salary_list = EmployeeSalary.objects.all()
    context = {"data":salary_list}

    return render(request, 'salaryrecords/index_salaryrecord.html', context)

def salary_add(request):

    sal_create_form = SalaryCreateForm()
    context = {"form": sal_create_form}

    if request.method == "POST":
        sal = EmployeeSalary()
        employee = Employee.objects.get(id=request.POST.get('employee'))
        sal.salary_amount = request.POST.get('salary_amount')
        sal.bonus_amount = request.POST.get('bonus_amount')
        sal.allowance = request.POST.get('bonus_amount')
        sal.tds_in_percent = request.POST.get('tds_in_percent')
        sal.start_date = request.POST.get('start_date')
        sal.end_date = request.POST.get('end_date')
        sal.employee= employee
        sal.save()

        messages.success(request, 'Salary added successfully')
        return redirect('sal-index')
    
    return render(request, 'salaryrecords/add_salaryrecord.html', context)

def salary_edit(request, id):
    data = EmployeeSalary. objects.get(id=id)
    employee = Employee.objects.all()
    context = {"data":data, "employee":employee}

    return render(request, 'salaryrecords/edit_salaryrecord.html',context)

def salary_show(request, id):
    data = EmployeeSalary.objects.get(id=id)
    context = {"data":data}
    return render(request, 'salaryrecords/show_salaryrecord.html',context)

def salary_delete(request, id):
    data = EmployeeSalary.objects.get(id=id)
    data.delete()

    messages.success(request, 'Salary deleted successfully')

    return redirect('sal-index')

def salary_update(request):
    if request.method == "POST":
        employee = Employee.objects.get(id=request.POST.get('employee'))
        sal= EmployeeSalary.objects.get(id= request.POST.get('id'))
        sal.salary_amount= request.POST.get('salary_amount')
        sal.bonus_amount = request.POST.get('bonus_amount')
        sal.allowance = request.POST.get('allowance')
        sal.tds_in_percent = request.POST.get('tds_in_percent')
        sal.start_date = request.POST.get('start_date')
        sal.end_date = request.POST.get('end_date')
        sal.employee=employee
        sal.save()

        messages.success(request, 'Salary details updated successfully')

        return redirect('sal-index')

    return render(request, 'salaryrecords/update_salaryrecord.html')


# function for salary section ends here  