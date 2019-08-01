from django.db import models
from django.contrib.auth.models import User
# from ..service.models import *

class Store(models.Model):
  # id auto
  store_id = models.CharField(max_length=5, primary_key=True)
  name = models.CharField(max_length=45)
  street_number = models.IntegerField()
  street_name = models.CharField(max_length=255)
  city = models.CharField(max_length=45)
  state = models.CharField(max_length=2)
  zip_code = models.CharField(max_length=5) 
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

class Department(models.Model):
  # id auto
  dept_id = models.CharField(max_length=3, primary_key=True)
  name = models.CharField(max_length=45)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
  # id auto
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dob = models.DateField()
  telephone = models.CharField(max_length=11)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Dept_Assignment(models.Model):
  user = models.ForeignKey(Employee, related_name="assigned_user_dept", on_delete=models.CASCADE)
  department = models.ForeignKey(Department, related_name="assigned_dept", on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Store_Assignment(models.Model):
  user = models.ForeignKey(Employee, related_name="assigned_user_store", on_delete=models.CASCADE)
  store = models.ForeignKey(Store, related_name="assigned_store", on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

