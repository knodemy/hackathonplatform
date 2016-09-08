from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
#from hackathons.models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm 
 
 
 #forms here
 
class PostForm(forms.Form):
    content = forms.CharField(max_length=256)
    created_at = forms.DateTimeField()


'''
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
'''     
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class ContactForm(forms.Form):
    first_name = forms.CharField(required = False)
    email = forms.EmailField(required = False)
    password = forms.CharField(widget=forms.PasswordInput())
