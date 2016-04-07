from django.shortcuts import render
from .models import Lesson


def index(request):
    return render(request, "index.html")


def lessons(request, lesson_number=1):
    return render(request, "lessons.html", {
        "lessons": Lesson.objects.all().order_by("lesson_number"),
        "lesson": Lesson.objects.get(lesson_number=lesson_number)
    })


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
