#-*- coding: utf-8 -*-
from CSN.form import LoginForm,signUpForm
from django.shortcuts import render
from CSN.models import LoginModel,Stuacc,Profile

def login(request):
   return render(request, 'login.html')

def login_info(request):
    if request.method == "POST":
      
         username= request.POST.get("email")
         password = request.POST.get("password")
         email = Stuacc.objects.get(email = username)
         pro=Profile.objects.select_related('Stuacc').get(Stuacc_id=email.id)
         
         if email:
            return render(request, 'login_info.html',{"student" : pro})
         else:
            return render(request,'error.html')
     
    else:
        return render(request,'login.html')

def sign_up(request):
   return render(request,'signup.html')

def register(request):
    context ={}
    # add the dictionary during initialization
    form = signUpForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "profile.html", context)
    
def logout(request):
   return render(request,'login.html')

def profile(request):
   form = profileForm(request.POST or None)
   
   if form.is_valid():
        form.save()
         
   context['form']= form
   return render(request, "profile.html", context)