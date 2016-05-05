from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import *
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
    return render(request, "forum.html",{
        "replyForm": ReplyForm(),
        "postForm": PostForm(),
        "posts": Post.objects.all()
    })


@login_required(login_url="/login/")
def post(request, post=-1):
    if request.method == "POST":
        form = PostForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Your post has an error please try again")
            return redirect(request.META['HTTP_REFERER'])
        unsaved_form = form.save(commit=False)
        unsaved_form.user = request.user
        unsaved_form.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        if post < 0:
            return redirect(request.META['HTTP_REFERER'])
        else:
            post = Post.objects.get(pk=post)


@login_required(login_url="/login/")
def add_reply(request, post):
    post = Post.objects.get(pk=post)
    form = ReplyForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Your post has an error please try again")
        return redirect(request.META['HTTP_REFERER'])
    unsaved_form = form.save(commit=False)
    unsaved_form.user = request.user
    unsaved_form.post = post
    unsaved_form.save()
    return redirect(request.META['HTTP_REFERER'])


def faq(request):
    return render(request, "faq.html")


@login_required(login_url='/login/')
def dashboard(request):
    user = UserProfile.objects.get(user=request.user)
    unfinished_lessons = Lesson.objects.all().order_by("lesson_number").exclude(id__in=user.lessons.all())
    return render(request, "dashboard.html", {
        "user": request.user,
        "profile": user,
        "completion_percentage": (len(user.lessons.all()) / float(len(Lesson.objects.all()))) * 100,
        "next": unfinished_lessons[0] if len(unfinished_lessons) > 0 else None
    })


@login_required(login_url='/login/')
def language_specific(request, title="Java"):
    languages = LanguageArticle.objects.all()
    specific_language = LanguageArticle.objects.get(title=title)
    return render(request, "language_specific.html",{
        "languages": languages,
        "specific_language": specific_language
    })


@login_required(login_url='/login/')
def quizes(request, quizID):
    quiz = Quiz.objects.get(pk=quizID)
    if request.method == "POST":
        for question in quiz.questions.all():
            if request.POST.get(question.question) != question.correct_answer:
                messages.add_message(request, messages.ERROR, 'Sorry you failed. Try again')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        messages.add_message(request, messages.INFO, 'Great job! You got it right! Check your homepage for new badges.')
        user = UserProfile.objects.get(user=request.user)
        lesson = Lesson.objects.get(pk=quiz.lesson.pk)
        badge = Badge.objects.get(pk=lesson.badge.pk)
        user.lessons.add(lesson)
        user.badges.add(badge)
        if lesson.lesson_number < 10:
            return redirect("/lessons/" + str(lesson.lesson_number + 1))
        else:
            return redirect("/lessons")
    else:
        return render(request, "quiz.html", {
            "quiz": quiz
        })
