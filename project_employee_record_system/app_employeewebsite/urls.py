from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_index, name = 'emp-index'),
    path('employees/show/<int:id>/', views.employee_show, name = 'emp-show'),
    path('employees/edit/<int:id>/', views.employee_edit, name ='emp-edit'),
    path('employees/delete/<int:id>/', views.employee_delete, name ='emp-delete'),
    path('employees/add/', views.employee_add, name= 'emp-add'),
    path('employee/update/', views.employee_update, name='emp-update')
]