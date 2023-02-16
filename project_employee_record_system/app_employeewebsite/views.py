from django.shortcuts import render

# Create your views here.
def employee_index(request):
    return render(request, 'employees/index_employee.html')

def employee_add(request):
    return render(request, 'employees/add_employee.html')

def employee_edit(request):
    return render(request, 'employees/edit_employee.html')

def employee_show(request):
    return render(request, 'employees/show.employee.html')