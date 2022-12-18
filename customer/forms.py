from django import forms
from django.forms import ModelForm
from owner.models import Carts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username=forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password=forms.CharField(label=" ",label_suffix=" ",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label=" ",label_suffix=" ",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    password2=forms.CharField(label=" ",label_suffix=" ",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm password"}))
    first_name= forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class": "form-control ", "placeholder": "First name"}))
    last_name= forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}))
    username= forms.CharField(label=" ",label_suffix=" ",widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    email= forms.CharField(label=" ",label_suffix=" ",widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "email"}))
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

#         widgets={
#             "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"First name"}),
#             "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Last name"}),
#             "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
#             "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"email"})
# }

class CartForm(forms.Form):
    qty=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

class OrderForm(forms.Form):
    delivery_address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"})) #Textarea():width ulla textbox



