# from django import forms
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z]\w{7,14}$')

# class UserForm(forms.ModelForm):
#   fname = forms.CharField(
#     label='First Name', 
#     widget=forms.TextInput(attrs={"placeholder": "Enter First Name"}))
#   lname = forms.CharField(
#     label='Last Name', 
#     widget=forms.TextInput(attrs={"placeholder": "Enter Last Name"}))
#   uname = forms.CharField(
#     label='Username', 
#     widget=forms.TextInput(attrs={"placeholder": "Enter Username"}))
#   em = forms.EmailField(
#     label='Business Email', 
#     widget=forms.TextInput(attrs={"placeholder": "Enter Email"}))
#   pw = forms.PasswordField(
#     label='Password', 
#     widget=forms.TextInput(attrs={"placeholder": "Enter New Password"}))
#   cpw = forms.PasswordField(
#     label='Confirm Password', 
#     widget=forms.TextInput(attrs={"placeholder": "Re-enter New Password"}))
  
#   class Meta:
#     model = User
#     fields = [
#       'fname',
#       'lname',
#       'uname',
#       'em',
#       'pw'
#     ]

class EmployeeManager(models.Manager):
  def first_name(self, postData):
    error = ""
    if len(postData)<1:
      error = "First name is required!"
    elif len(postData)<2:
      error = "First name must be at least 2 characters!"
    return error

  def last_name(self, postData):
    error = ""
    if len(postData)<1:
      error = "Last name is required!"
    elif len(postData)<2:
      error = "Last name must be at least 2 characters!"
    return error

  def email(self, postData):
    error = {
      "error": "",
      "class": ""
    }
    error['class'] = "text-danger"
    check = User.objects.filter(email=postData)
    new = check.values()
    if len(postData)<1:
      error['error'] = "Email is required!"
    elif not EMAIL_REGEX.match(postData):
      error['error'] = "Invalid email!"
    elif new.exists():
      error['error'] = "Email has been taken"
    else:
      error['error'] = "This email is available"
      error['class'] = "text-success"
    return error

  def pword(self, postData):
    error = {
      "error": "",
      "class": ""
    }
    error['class'] = "text-danger"
    if len(postData)<1:
      error['error'] = "Password is required!"
    elif not PW_REGEX.match(postData):
      error['error'] = "The password's first character must be a letter, it must contain 8-15 characters with only letters, numbers and the underscore may be used"
    else:
      error['error'] = "Strong Password"
      error['class'] = "text-success"
    return error
    
  def c_pword(self, postData1, postData2):
    error = {
      "error": "",
      "class": ""
    }
    print (">>>>>>",postData1, postData2)
    error['class'] = "text-danger"
    if len(postData1)<1:
      error['error'] = "Password Confirm is required!"
    elif postData1 != postData2:
      error['error'] = "Passwords must match!"
    else:
      error['error'] = "Passwords match"
      error['class'] = "text-success"
    return error

  def dob(self, postData):
    error = ""
    if len(postData) < 1:
      error = "Date of Birth is required!"
    else:
      dob = datetime.strptime(postData, "%Y-%m-%d")
      if dob > datetime.now():
        error = "Date of Birth must be in the past"       
      else:
        today = date.today() 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
        if age < 13:
          error = "You must be at least 13 to register" 
    return error

  def register(self, postData):
    is_valid = True,
    #validations
    if len(postData['fname'])<1:
      is_valid = False
    elif len(postData['fname'])<2:
      is_valid = False
    if len(postData['lname'])<1:
      is_valid = False
    elif len(postData['lname'])<2:
      is_valid = False
    if len(postData['em'])<1:
      is_valid = False
    elif not EMAIL_REGEX.match(postData['em']):
      is_valid = False
    else:
      user = User.objects.filter(email=postData['em'].lower())
      if len(user) > 0:
        is_valid = False
    if len(postData['pw'])<1:
      is_valid = False 
    elif len(postData['pw'])<8:
      is_valid = False
    if len(postData['cpw'])<1:
      is_valid = False
    elif postData['pw'] != postData['cpw']:
      is_valid = False
    if len(postData['dob']) < 1:
      is_valid = False
    else:
      dob = datetime.strptime(postData['dob'], "%Y-%m-%d")
      if dob > datetime.now():
        is_valid = False  
      else:
        today = date.today() 
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 
        if age < 13:
          is_valid = False
    if len(postData['gender']) < 1:
      is_valid = False
    if is_valid:
      User.objects.create(
          first_name=postData["fname"].title(),
          last_name=postData["lname"].title(),
          username=postData["uname"].lower(),
          email=postData["em"].lower())
      user=User.objects.last()
      user.set_password(postData['pw'])
      user.save()   
      Employee.objects.create(
          user=user,
          dob=postData["dob"],
          gender=postData["gender"],
          dept=postData["dept"],
          title=postData["title"],
          level=postData["level"],
          telephone=postData["phone"])
      
      if postData["level"] == "Admin":
        user.is_staff = True
      if postData["level"] == "Superuser":
        user.is_staff = True
        user.is_superuser = True
    else:
      is_valid = False
    return is_valid

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
  gender = models.CharField(max_length=10)
  dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employee_dept")
  title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True, related_name="employee_title")
  level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, related_name="employee_level")
  telephone = models.CharField(max_length=11)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = EmployeeManager()
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
  

