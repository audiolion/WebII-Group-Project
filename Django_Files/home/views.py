from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import *


def index(request):
    if request.user.is_authenticated():
        return redirect("/dashboard")
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
    user = UserProfile.objects.get(user=request.user)
    unfinished_lessons = Lesson.objects.all().order_by("lesson_number").exclude(id__in = user.lessons.all())
    return render(request, "dashboard.html", {
        "user": request.user,
        "profile": user,
        "completion_percentage": (len(user.lessons.all())/float(len(Lesson.objects.all()))) * 100,
        "next": unfinished_lessons[0] if len(unfinished_lessons) > 0 else None
    })


@login_required(login_url='/login/')
def language_tools(request):
    return render(request, "language_tools.html")


@login_required(login_url='/login/')
def quizes(request, quizID):
    quiz = Quiz.objects.get(pk=quizID)
    if request.method == "POST":
        for question in quiz.questions.all():
            if request.POST.get(question.question) != question.correct_answer:
                messages.add_message(request, messages.ERROR, 'Sorry you failed. Try again')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        messages.add_message(request, messages.INFO, 'Great job! You got it right!')
        user = UserProfile.objects.get(user=request.user)
        lesson = Lesson.objects.get(pk = quiz.lesson.pk)
        user.lessons.add(lesson)
        if lesson.lesson_number < 10:
            return redirect("/lessons/"+str(lesson.lesson_number+1))
        else:
            return redirect("/lessons")
    else:
        return render(request, "quiz.html", {
            "quiz": quiz
        })
