from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_index, name = 'emp-index'),
    path('employees/show/', views.employee_show, name = 'emp-show'),
    path('employees/edit/', views.employee_edit, name ='emp-edit'),
    path('employees/add/', views.employee_add, name= 'emp-add'),
]