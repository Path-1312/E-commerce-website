from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    class Media:
        js = ('admin/js/subcategory.js',)
        
        