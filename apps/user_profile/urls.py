from django.urls import path
from . import views 

urlpatterns = [
  path('', views.index),
  path('profile_create/', views.profile_create),
  path('profile_create_process/', views.profile_create_process),
  path('profile_view/<int:u_id>/', views.profile_view),
  path('profile_edit/<int:u_id>/', views.profile_edit),
  path('profile_active/<int:u_id>/', views.profile_active),
  path('profile_inactive/<int:u_id>/', views.profile_inactive),
  path('profile_delete/<int:u_id>/', views.profile_delete),

  path('profile_update_process/<int:u_id>/', views.profile_update_process),
  path('store_assign/<int:store_id>/<int:user_id>/', views.store_assign),
  path('store_unassign/<int:store_id>/<int:user_id>/', views.store_unassign),

  # AJAX Validation Paths
  path('fname/', views.fname), #Ajax 
  path('lname/', views.lname), #Ajax
  path('email/', views.email), #Ajax 
  path('pword/', views.pword), #Ajax 
  path('c_pword/', views.c_pword), #Ajax 
  path('dob/', views.dob), #Ajax 
]