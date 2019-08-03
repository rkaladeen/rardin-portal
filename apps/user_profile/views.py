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
  user_to_edit = Employee.objects.get(id=u_id)
  all_stores = Store.objects.all()
  store_assigned = Employee.objects.get(id=u_id).stores_assigned.all()
  store_not_assigned = all_stores.difference(store_assigned)
  # Sorting Differences
  all_depts = Department.objects.all()
  all_titles = Title.objects.all()
  all_levels = Level.objects.all()
  context = {
    "one_user": user_to_edit,
    "all_depts": all_depts,
    "all_titles": all_titles,
    "all_levels": all_levels,
    "all_stores": all_stores,
    "stores_assigned": store_assigned,
    "stores_not_assigned": store_not_assigned,
  }
  return render(request, "user_profile/profile_edit.html", context)

def profile_inactive(request, u_id):
  user_to_disactivate = User.objects.get(id=u_id)
  user_to_disactivate.is_active = False
  user_to_disactivate.save()
  return redirect("/user_profile")

def profile_active(request, u_id):
  user_to_activate = User.objects.get(id=u_id)
  user_to_activate.is_active = True
  user_to_activate.save()
  return redirect("/user_profile")

def profile_delete(request, u_id):
  user_to_delete = User.objects.get(id=u_id)
  user_to_delete.delete();
  return redirect("/user_profile")

# Action Functions
def profile_update_process(request, u_id):
  user_to_update = Employee.objects.get(id=u_id)
  
  user_to_update.user.first_name = request.POST['fname']
  user_to_update.user.last_name = request.POST['lname']
  user_to_update.user.email = request.POST['em']
  
  dept = Department.objects.get(name=request.POST['dept'])
  title = Title.objects.get(name=request.POST['title'])
  level = Level.objects.get(name=request.POST['level'])

  # Update method only works with filter method
  Employee.objects.filter(id=u_id).update(dept=dept) 
  Employee.objects.filter(id=u_id).update(title=title)
  Employee.objects.filter(id=u_id).update(level=level)
  
  # user_to_update.save()
  user_to_update.user.save()
  
  return redirect(f"/user_profile/profile_view/{u_id}")

@login_required(login_url='/login')
def store_assign(request, store_id, user_id):
  store_to_assign = Store.objects.get(store_id=store_id)
  user_to_assign_store = Employee.objects.get(id=user_id)
  store_to_assign.employees.add(user_to_assign_store)
  store_to_assign.save()
  print(f"{user_to_assign_store.user.first_name} assigned to store {store_to_assign.store_id}")
  
  all_stores = Store.objects.all()
  store_assigned = user_to_assign_store.stores_assigned.all()
  store_not_assigned = all_stores.difference(store_assigned)
  context = {
    "one_user": user_to_assign_store,
    "stores_assigned": store_assigned,
    "stores_not_assigned": store_not_assigned,
  }
  return render(request, "partials/assignments.html", context)

@login_required(login_url='/login')
def store_unassign(request, store_id, user_id):
  store_to_unassign = Store.objects.get(store_id=store_id)
  user_to_unassign_store = Employee.objects.get(id=user_id)
  store_to_unassign.employees.remove(user_to_unassign_store)
  store_to_unassign.save()
  print(f"{user_to_unassign_store.user.first_name} Unassigned from store {store_to_unassign.store_id}")
  
  all_stores = Store.objects.all()
  store_assigned = user_to_unassign_store.stores_assigned.all()
  store_not_assigned = all_stores.difference(store_assigned)
  context = {
    "one_user": user_to_unassign_store,
    "stores_assigned": store_assigned,
    "stores_not_assigned": store_not_assigned,
  }
  return render(request, "partials/assignments.html", context)