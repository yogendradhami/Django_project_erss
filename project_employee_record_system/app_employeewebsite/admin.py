from django.contrib import admin
from .models import Department
from .models import Employee
from .models import EmployeeSalary

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)