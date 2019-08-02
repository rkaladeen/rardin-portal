from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *

def index(request):
  return render(request, "main/index.html")
