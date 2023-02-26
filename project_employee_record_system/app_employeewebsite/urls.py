from django.urls import path
from . import views

urlpatterns = [

    # ''' urls for employee section start here '''
    
    path('employees/', views.employee_index, name = 'emp-index'),

    path('employees/show/<int:id>/', views.employee_show, name = 'emp-show'),

    path('employees/edit/<int:id>/', views.employee_edit, name ='emp-edit'),

    path('employees/delete/<int:id>/', views.employee_delete, name ='emp-delete'),

    path('employees/add/', views.employee_add, name= 'emp-add'),

    path('employee/update/', views.employee_update, name='emp-update'),

    # ''' urls for employee section ends here '''



    # ''' urls for department section starts here '''

    path('department/', views.department_index, name = 'dprt-index'),

    path('department/show/<int:id>/', views.department_show, name = 'dprt-show'),

    path('department/edit/<int:id>/', views.department_edit, name ='dprt-edit'),

    path('department/delete/<int:id>/', views.department_delete, name ='dprt-delete'),

    path('department/add/', views.department_add, name= 'dprt-add'),

    path('department/update/', views.department_update, name='dprt-update'),


    # ''' urls for department section ends here '''



    # ''' urls for salary section starts here '''

    path('salary/', views.salary_index, name='sal-index'),

    # ''' urls for salary section ends here '''
 
]