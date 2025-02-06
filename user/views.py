from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import *

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user_auth = authenticate(username=user_name,password=password)
        if user_auth:
            login(request,user_auth)
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')

    return render(request,"user/login_page.html")

def signup_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        

        # validation
        if not user_name or not password or not email or not phone :
            messages.error(request,'All fields are required')
        elif password != confirm_password:
            messages.error(request,'Password mismatch')
        elif Customer.objects.filter(phone=phone).exists():
            messages.error(request,'Phone number already exists')
            return redirect('signup_user')
        
        try:
            user = User.objects.create_user(
                username=user_name,
                email=email,
                password=password
                )
            user.save()
            dealer_obj = Customer.objects.create(
                user = user,
                phone = phone,
                
            )
            login(request,user)
            return redirect('home')
        except Exception as e:
            messages.error(request,str(e))
        
        

    return render(request,"user/signup_page.html")

def logut_user(request):
    logout(request)
    return redirect('login_user')


def account(request):
    return render(request,'user/account_manage.html')