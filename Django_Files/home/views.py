from django.shortcuts import render

from .models import *
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


def faq(request):
    return render(request, "faq.html")


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, "dashboard.html")


@login_required(login_url='/login/')
def language_tools(request):
    return render(request, "language_tools.html")


@login_required(login_url='/login/')
def quizes(request, quizID):
    quiz = Quiz.objects.get(pk=quizID)
    if request.method == "POST":
        for question in quiz.questions.all():
            if request.POST.get(question.question) == question.correct_answer:
                print(True)
            else:
                print(False)
    return render(request, "quiz.html", {
        "quiz": quiz
    })