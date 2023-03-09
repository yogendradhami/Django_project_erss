"""project_employee_record_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path url for admin starts here

    path('admin/', admin.site.urls),
    
    # path url for admin ends here

    # path urls for employees starts here

    path('employee/', include('app_employeewebsite.urls')),
    path('', include('app_employeewebsite.urls')), 
    # incase if need to load via base url

     # path urls for employees ends here

    # path ulrs for authentication starts here

    path('authentication/', include('authentication.urls')),

    # path urls for authentication ends here

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/ers/', include('ers_api.urls')),
]


