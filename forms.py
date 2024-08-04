# project_manager/forms.py from django 
import forms from 
django.contrib.auth.models import User 
from .models import UserProfile, Project 
class UserLoginForm(forms.Form): 
username = forms.CharField() 
 password = forms.CharField(widget=forms.PasswordInput) 
class UserRegistrationForm(forms.ModelForm): password = 
forms.CharField(label='Password', widget=forms.PasswordInput) class Meta: 
 model = User 
 fields = ['first_name', 'last_name', 'username'] 
class ProjectCreationForm(forms.ModelForm): 
class Meta: 
 model = Project 
 fields = ['name', 'description', 'required_participants'] 
class ProfileEditForm(forms.ModelForm): 
class Meta: 
 model = UserProfile 
 fields = ['phone_number', 'gender'] 
8
class ProjectJoinForm(forms.Form): project_ids = 
forms.ModelMultipleChoiceField(queryset=Project.objects.all(), 
widget=forms.CheckboxSelectMultiple)
