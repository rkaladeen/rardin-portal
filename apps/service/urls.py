from django.urls import path 
from . import views 

urlpatterns = [
  path('', views.index),
  # Ticket MS
  path('equip_ticket_form/', views.equip_ticket_form),
  path('gen_ticket_form/', views.gen_ticket_form),
  path('tech_ticket_form/', views.tech_ticket_form),
  path('create_ticket/', views.create_ticket),
  path('ticket_delete/<int:tkt_id>/', views.ticket_delete),
  path('ticket_update/<int:tkt_id>/', views.ticket_update),
  path('ticket_update_process/<int:tkt_id>/', views.ticket_update_process),
  path('ticket_view/<int:tkt_id>/', views.ticket_view),
  
  path('create_message/<int:tkt_id>/', views.create_message),
  path('delete_message/<int:msg_id>/', views.delete_message),
]