from django.contrib import admin

from .models import Badge, Goal, Reply, Post, UserProfile, Lesson, Question, Quiz, LanguageArticle

# Register your models here.

myModels = [Badge, Goal, Reply, Post, UserProfile, Lesson, Question, Quiz, LanguageArticle]  # iterable list

admin.site.register(myModels)
