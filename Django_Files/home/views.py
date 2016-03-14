from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .models import UserProfile
from .forms import LoginForm, RegisterForm


def index(request):
    return render(request, "index.html")



