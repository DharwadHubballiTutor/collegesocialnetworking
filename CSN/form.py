#-*- coding: utf-8 -*-
from django import forms
from .models import Stuacc, Profile

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Stuacc.objects.filter(name = email)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username
   
class signUpForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Stuacc
 
        # specify fields to be used
        fields = [
            "firstname",
            "lastname",
            "email",
            "password",
            "confirmpassword",
            "iam",
            "dob"
        ]
        
class profileForm(forms.ModelForm):
    class Meta:
        
        model:Profile
        
        fields = [
            "userid",
            "relstat",
            "city",
            "state",
            "pincode",
            "image",
            "hschool",
            "coluni",
            "course",
            "Stuacc"
        ]