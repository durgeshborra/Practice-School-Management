# project_manager/views.py from django.shortcuts 
import render, redirect from django.contrib.auth 
import authenticate, login from .forms import 
UserLoginForm, UserRegistrationForm, 
ProjectCreationForm from .models import Project
def login_view(request): if request.method 
== 'POST': form = 
UserLoginForm(request.POST) if 
form.is_valid(): 
 username = form.cleaned_data['username'] password = 
form.cleaned_data['password'] user = 
authenticate(username=username, password=password) if 
user is not None: login(request, user) return 
redirect('home') else: 
 form = UserLoginForm() 
 return render(request, 'login.html', {'form': form}) 
def register_view(request): if 
request.method == 'POST': 
 form = UserRegistrationForm(request.POST) 
if form.is_valid(): user = form.save() 
 UserProfile.objects.create(user=user, phone_number=request.POST['phone_number'], 
gender=request.POST['gender']) 
 return redirect('login') 
else: 
 form = UserRegistrationForm() 
 return render(request, 'register.html', {'form': form}) 
def home_view(request): 
 projects = Project.objects.all() 
 return render(request, 'home.html', {'projects': projects}) 
def create_project_view(request): 
if request.method == 'POST': 
 form = ProjectCreationForm(request.POST) 
if form.is_valid(): 
 project = form.save(commit=False) 
project.creator = request.user 
project.save() return 
redirect('login') else: 
 form = ProjectCreationForm() 
 return render(request, 'create_project.html', {'form': form}) 
def view_my_projects(request): 
7
 projects = Project.objects.filter(creator=request.user) 
return render(request, 'login.html', {'projects': projects}) 
def view_all_projects(request): projects = 
Project.objects.all() return render(request, 'login.html', 
{'projects': projects}) 
def edit_profile(request): 
 # Handle profile editing logic here 
return render(request, 'login.html') 
