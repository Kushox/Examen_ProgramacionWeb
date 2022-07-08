
from django import forms 
from .models import Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        
        widgets= {
            "fechaProducto": forms.SelectDateWidget()
        }
        

class UserRegisterForm(UserCreationForm): 
    username= forms.CharField(label='username', max_length=40)                                       
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
        help_texts ={k:"" for k in fields}