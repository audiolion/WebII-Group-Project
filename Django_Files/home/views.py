from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "index.html")


def lessons(request):
    return render(request, "lessons.html")


def reference(request):
    return render(request, "reference.html")


def forum(request):
    return render(request, "forum.html")


def dashboard(request):
    return render(request, "dashboard.html")


def language_tools(request):
    return render(request, "language_tools.html")


def about_us(request):
    return render(request, "about_us.html")
