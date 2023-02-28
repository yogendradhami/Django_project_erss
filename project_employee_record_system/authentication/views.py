from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth import login as authlogin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

# Create your views here.

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request, "You're logged out!!")
        return redirect('user_login')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    

    def post(self, request):
        username  = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('emp-index')
        else:
            messages.error(request,  'Invaid username or password!')
            return  redirect('user_login')

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
            send_mail(
                'Account Creation  | ERS',  #subject
                'Your account has been created! \n Welcome ' + data.username,  #messagee
                'yogendradhami6@gmail.com',  # sender
                [data.email] # reciever
            )
            return redirect('user_login')