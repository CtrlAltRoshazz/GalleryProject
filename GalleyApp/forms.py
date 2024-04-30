from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

from . models import ImageModel

from django import forms

class RegisterForm(UserCreationForm):
    
    password1 = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    password2 = forms.CharField(label='Confirm Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'username' , 'email']
        
        labels = {
            'first_name':'Enter your First Name',
            'last_name':'Enter your Last Name',
            'Username':'Enter your Username',
            'email':'Enter your Email-ID',
        }
        
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Enter Your Username' , widget=forms.TextInput(attrs={'class':'form-control'}))
    
    password = forms.CharField(label='Enter Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        
        fields = ['username' , 'password']
        
class AddImageForm(forms.ModelForm):
    
    class Meta:
        model =  ImageModel
        fields = ['title' , 'desc' , 'cat' , 'image']
        
        labels = {
            'title':'Enter Image Title',
            'desc':'Enter Image Discription',
            'cat':'Select Image Category',
            'image':'Upload Image'
        }
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }
        