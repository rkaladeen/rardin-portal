from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
  # id auto
  dept_id = models.CharField(max_length=3, primary_key=True)
  name = models.CharField(max_length=45)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Title(models.Model):
  title_id = models.CharField(max_length=3, primary_key=True)
  name = models.CharField(max_length=45)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Level(models.Model):
  level_id = models.CharField(max_length=1, primary_key=True)
  name = models.CharField(max_length=45)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Employee(models.Model):
  # id auto
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dob = models.DateField()
  dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employee_dept")
  title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True, related_name="employee_title")
  level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name="employee_level")
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
  

