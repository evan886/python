from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login  #1
from .forms import LoginForm





def user_login(request):  #2
    if request.method == "POST":   #3
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("Welcome,You have been authenticated successfully.")
            else:
                return HttpResponse("Sorry, Your username or password is not right.")
        else:
            return HttpResponse("Invalidl login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})

            
               
               
            
            
            
            
# Create your views here.
