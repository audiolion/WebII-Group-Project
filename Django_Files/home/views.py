from django.shortcuts import render
from .models import Lesson
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def about_us(request):
    return render(request, "about_us.html")


@login_required(login_url='/login/')
def lessons(request, lesson_number=1):
    return render(request, "lessons.html", {
        "lessons": Lesson.objects.all().order_by("lesson_number"),
        "lesson": Lesson.objects.get(lesson_number=lesson_number)
    })


@login_required(login_url='/login/')
def reference(request):
    return render(request, "reference.html")


@login_required(login_url='/login/')
def forum(request):
    return render(request, "forum.html")


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, "dashboard.html")


@login_required(login_url='/login/')
def language_tools(request):
    return render(request, "language_tools.html")
