from django.contrib import admin
from .models import Department
from .models import Employee
from .models import EmployeeSalary

# Register your models here.
class AdminEmployee(admin.ModelAdmin):
    list_display= ("full_name", "join_date", "email","contact")
    search_field = ("fill_name", "email")
    list_filter =  ("full_name", "email")
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)

# to rename the admin panel records
admin.site.site_header = 'ERS'
admin.site.site_title = 'ERS'
admin.site.index_title = 'Admin Panel'