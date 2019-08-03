from django.db import models
# from django.contrib.auth.models import User
from ..main.models import *

class Ticket(models.Model):
  store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
  submit_by = models.CharField(max_length=45)
  t_type = models.CharField(max_length=45)
  short_desc = models.CharField(max_length=255)
  desc = models.TextField()
  ts = models.TextField()
  status = models.CharField(max_length=45, default = 'Not Acknowledged')
  assign_to = models.CharField(max_length=45, default = 'Unassigned')
  priority = models.CharField(max_length=45, default = 'Unassigned')
  tech_note = models.TextField(default='')
  res_note = models.TextField(default='')
  creator = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="creator_ticket")
  created_at = models.DateTimeField(auto_now_add=True)
  last_view = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="last_view_ticket")
  viewed_at = models.DateTimeField(auto_now=True)
  last_update = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="last_update_ticket") 
  updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
  # id auto
  sender = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
  ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  # id auto
  sender = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
  ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
  message = models.ForeignKey(Message, on_delete=models.CASCADE)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


