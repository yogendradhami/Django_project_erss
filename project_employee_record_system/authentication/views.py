from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    

    def post(self, request):
        username  = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username,password)
        if user:
            messages.succes(request, 'Login successfully')
            return redirect('emp-index')
        else:
            messages.error(request,  'Invaid username or password!')
            return  redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request,'authentication/register.html')

    def post(self, request):
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email =  request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')

        try:
            user=  User.objects.get(username=username)
            if user:
                messages.error(request, 'Username already exists. Try with new one!')
                return redirect('register')
        except:
            data =User.objects.create_user(first_name = first_name, last_name = last_name, email=email, username=username,password=password)

            messages.success(request,'Accocunt  created successfully!')
            return redirect('login')