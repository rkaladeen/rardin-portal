from django.urls import path
from . import views 

urlpatterns = [
  path('', views.index),
  path('profile_view/<int:u_id>/', views.profile_view),
  path('profile_edit/<int:u_id>/', views.profile_edit),
  path('profile_delete/<int:u_id>/', views.profile_delete),

  path('profile_update_process/<int:u_id>/', views.profile_update_process),

]