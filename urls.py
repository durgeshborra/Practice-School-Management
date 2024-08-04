# project_management_system/urls.py 
from django.contrib import admin from 
django.urls import path 
from emp_app.views import login_view, register_view, home_view, create_project_view 
urlpatterns = [ 
 path('admin/', admin.site.urls), path('', 
login_view, name='login'), path('register/', 
register_view, name='register'), path('home/', 
home_view, name='home'), 
 path('create_project/', create_project_view, name='create_project'), 
]
