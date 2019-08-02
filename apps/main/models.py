from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
  # id auto
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dob = models.DateField()
  department = models.CharField(max_length=45, default="")
  job_title = models.CharField(max_length=45, default="")
  user_type = models.CharField(max_length=45, default="User")
  telephone = models.CharField(max_length=11)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # Stores Assigned attribute added from M2M relationship

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
  employees = models.ManyToManyField(Employee, related_name="stores_assigned")
  
class Department(models.Model):
  # id auto
  dept_id = models.CharField(max_length=3, primary_key=True)
  name = models.CharField(max_length=45)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Position(models.Model):
  job_id = models.CharField(max_length=3, primary_key=True)
  job_title = models.CharField(max_length=45)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
