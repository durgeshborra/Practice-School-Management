# project_manager/models.py 
from django.contrib.auth.models import User from 
django.db import models 
class Project(models.Model): name = 
models.CharField(max_length=100) 
description = models.TextField() 
required_participants = models.IntegerField() 
 status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 
'Completed')]) 
 creator = models.ForeignKey(User, on_delete=models.CASCADE, 
related_name='created_projects') participants = 
models.ManyToManyField(User, related_name='joined_projects') 
class UserProfile(models.Model): user = 
models.OneToOneField(User, on_delete=models.CASCADE) 
phone_number = models.CharField(max_length=15) gender = 
models.CharField(max_length=10) 
class ProjectJoinRequest(models.Model): user = 
models.ForeignKey(User, on_delete=models.CASCADE) project = 
models.ForeignKey(Project, on_delete=models.CASCADE) 
 status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 
'Accepted'), ('rejected', 'Rejected')]) 
class ProjectUpdate(models.Model): 
 project = models.ForeignKey(Project, on_delete=models.CASCADE) 
update_text = models.TextField() 
9
 timestamp = models.DateTimeField(auto_now_add=True)
