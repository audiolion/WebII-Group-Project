from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from .models import UserProfile
from .forms import LoginForm, RegisterForm


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            login(request, user)
        except:
            messages.error("Username or password is incorrect")
            return redirect(request.META['HTTP_REFERER'])
        return redirect("/")
    else:
        return render(request, "form.html", {
            'form': LoginForm(),
            "title": "Login"
        })


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if (form.is_valid()):
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            email=form.cleaned_data.get('email'),
                                            password=form.cleaned_data.get('password'))
            user.save()
            new_user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password'))
            user_profile = UserProfile(user_id=new_user.id)
            user_profile.save()
            try:
                login(request, new_user)
            except:
                messages.error("There has been an issue with your registration please try again.")
                return redirect(request.META['HTTP_REFERER'])
            return redirect("/")
        else:
            messages.error("There has been an issue with your registration please try again.")
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, "form.html", {
            'form': RegisterForm(),
            "title": "Register"
        })


def logout_view(request):
    logout(request)
    return redirect("/")
