from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ..main.models import *
from ..service.models import *
from .models import *

@login_required(login_url='/login')
def index(request):
  context = {
    "users": Employee.objects.all(),
    }
  return render(request, "user_profile/index.html", context)

@login_required(login_url='/login')
def profile_view(request, u_id):
  context = {
    "one_user": Employee.objects.get(id=u_id)
  }
  return render(request, "user_profile/profile_view.html", context)

@login_required(login_url='/login')
def profile_edit(request, u_id):
  all_stores = Store.objects.all()
  store_assigned = Employee.objects.get(id=u_id).stores_assigned.all()
  store_not_assigned = all_stores.difference(store_assigned)
  context = {
    "one_user": Employee.objects.get(id=u_id),
    "dept_list": Department.objects.all(),
    "stores_assigned": store_assigned,
    "stores_not_assigned": store_not_assigned,
  }
  return render(request, "user_profile/profile_edit.html", context)

def profile_delete(request, u_id):
  pass

# Action Functions
def profile_update_process(request, u_id):
  user_to_update = Employee.objects.get(id=u_id)
  
  user_to_update.user.first_name = request.POST['fname']
  user_to_update.user.last_name = request.POST['lname']
  user_to_update.user.email = request.POST['em']
  user_to_update.department = request.POST['dept']
  user_to_update.job_title = request.POST['title']
  user_to_update.user_type = request.POST['type']
  
  user_to_update.save()
  user_to_update.user.save()
  

  return redirect(f"/user_profile/profile_view/{u_id}")
