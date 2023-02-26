from django import forms
from .models import Employee
from .models import Department

class EmployeeCreateForm(forms.ModelForm):
    """ """
    class Meta:
        fields = "__all__"
        # field = ("full_name", "contact")
        model = Employee

class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Department
