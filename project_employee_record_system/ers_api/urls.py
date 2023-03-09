from django.urls import path
from .views import EmployeeApiView,EmployeeApiIdView
urlpatterns = [
    path('employee/', EmployeeApiView.as_view()),
    path('employee/<int:id>/', EmployeeApiIdView.as_view()),
]