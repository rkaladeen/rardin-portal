from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ..main.models import *
from .models import *

@login_required(login_url='/login')
def index(request):
  context = { "tickets": Ticket.objects.all().order_by('-created_at') }
  return render(request, "service/service.html", context)

@login_required(login_url='/login')
def equip_ticket_form(request):
  user = Employee.objects.get(id=request.user.id)
  context = {"store_assigned": user.stores_assigned.all().order_by('store_id')}
  return render(request, "service/equip_ticket.html", context)

@login_required(login_url='/login')
def gen_ticket_form(request):
  user = Employee.objects.get(id=request.user.id)
  context = {"store_assigned": user.stores_assigned.all().order_by('store_id')}
  return render(request, "service/gen_ticket.html", context)

@login_required(login_url='/login')
def tech_ticket_form(request):
  user = Employee.objects.get(id=request.user.id)
  context = {"store_assigned": user.stores_assigned.all().order_by('store_id')}
  return render(request, "service/tech_ticket.html", context)

def create_ticket(request):
  user = Employee.objects.get(id=request.user.id)
  creator = Employee.objects.get(id=user.id)
  
  string = request.POST['store_id']
  for s in string.split(): 
    if s.isdigit():
      store_id = s
  
  store=Store.objects.get(store_id=store_id)
  submit_by=request.POST['submit_by']
  short_desc=request.POST['short_desc']
  desc=request.POST['desc']
  ts=request.POST['ts']
  t_type=request.POST['t_type']
  # Move to Models
  Ticket.objects.create(store=store, submit_by=submit_by, t_type=t_type, short_desc=short_desc, desc=desc, ts=ts, creator=creator, last_view=creator, last_update=creator)
  return redirect("/service")

def ticket_delete(request, tkt_id):
  ticket_to_delete = Ticket.objects.get(id=tkt_id)
  ticket_to_delete.delete();
  return redirect("/service")

@login_required(login_url='/login')
def ticket_update(request, tkt_id):
  ticket = Ticket.objects.get(id=tkt_id)
  dept_to_assign = Department.objects.get(name=ticket.t_type)
  context = {
    "ticket": Ticket.objects.get(id=tkt_id),
    "tech_list": Employee.objects.filter(dept=dept_to_assign)
  }
  
  return render(request, "service/ticket_update.html", context)

def ticket_update_process(request, tkt_id):
  user = Employee.objects.get(id=request.user.id)
  ticket_to_update = Ticket.objects.get(id=tkt_id)
  ticket_to_update.priority = request.POST['priority']
  ticket_to_update.status = request.POST['status']
  ticket_to_update.assign_to = request.POST['assign_to']
  ticket_to_update.tech_note = request.POST['tech_note']
  ticket_to_update.res_note = request.POST['res_note']
  ticket_to_update.last_update = user
  ticket_to_update.save()
  return redirect(f"/service/ticket_view/{tkt_id}/")

@login_required(login_url='/login')
def ticket_view(request, tkt_id):
  user = Employee.objects.get(id=request.user.id)
  ticket_to_view = Ticket.objects.get(id=tkt_id)
  ticket_to_view.last_view = user
  ticket_to_view.save()
  context = {
    "ticket": Ticket.objects.get(id=tkt_id),
    "messages": Message.objects.filter(ticket=ticket_to_view)
    }
  return render(request, "service/ticket_view.html", context)

def create_message(request, tkt_id):
  sender = Employee.objects.get(id=request.user.id)
  ticket_to_add_message = Ticket.objects.get(id=tkt_id) 
  Message.objects.create(
    sender = sender,
    ticket = ticket_to_add_message,
    message = request.POST['message']
  )
  return render(request, 'partials/message.html', {"messages": Message.objects.filter(ticket=ticket_to_add_message)})
  
def delete_message(request, msg_id):
  message_to_delete = Message.objects.get(id=msg_id)
  message_to_delete.delete()
  ticket = message_to_delete.ticket

  return render(request, 'partials/message.html', {"messages": Message.objects.filter(ticket=ticket)})

