from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout #For Authentication related modules
from django.contrib import messages

# Email Imports
from django.core.mail import send_mail, EmailMessage
from AMC_Demo.settings import EMAIL_HOST_USER


def loginpage(request):
    # if request.method == "POST":
    #     email = request.POST.get('user')
    #     password = request.POST.get('pass')
    #     print(email, password)

    #     user  = authenticate(request, username = email, password = password)

    #     if user is not None:
    #         login(request, user)
    #         # Redirect to a success page or do further processing
    #         return redirect('dashboard')
    #     else:
    #         # Authentication failed, handle the error
    #         return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})


    return HttpResponse("<h1> Aa Web Site Chalu..... </h1>")