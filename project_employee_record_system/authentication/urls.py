from django.urls  import path
from .views import LoginView, RegisterView, LogoutView
urlpatterns = [
    path('login/',LoginView.as_view(), name= 'user_login'),
    path('logout/',LogoutView.as_view(), name= 'logout'),
    path('register/', RegisterView.as_view(), name = 'register'),

]