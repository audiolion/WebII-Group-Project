import datetime

from django.contrib.auth.models import User
from django.db.models import Model
from django.db.models.fields import IntegerField, CharField, DateField, BooleanField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField, OneToOneField


class Badge(Model):
    name = CharField(max_length=50)
    picture = ImageField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Goal(Model):
    start_date = DateField(default=datetime.date.today())
    end_date = DateField(default=None, null=True)
    lessons_completed = IntegerField(default=None, null=True)
    remind_me = BooleanField(default=True)


class Reply(Model):
    user = OneToOneField(User)
    text = TextField()
    date = DateField(default=datetime.date.today())

    def __str__(self):
        return u'{0}\n{1}'.format(self.user.username, self.text[:50])

    def __unicode__(self):
        return u'{0}\n{1}'.format(self.user.username, self.text[:50])


class Post(Model):
    user = OneToOneField(User)
    text = TextField()
    # Upvote/Stars/Karma
    replies = ManyToManyField(Reply)
    date = DateField(default=datetime.date.today())

    def __str__(self):
        return u'{0}\n{1}'.format(self.user.username, self.text[:50])

    def __unicode__(self):
        return u'{0}\n{1}'.format(self.user.username, self.text[:50])


class Question(Model):
    question = TextField()
    answer1 = CharField(max_length=200)
    answer2 = CharField(max_length=200)
    answer3 = CharField(max_length=200)
    answer4 = CharField(max_length=200)
    correct_answer = CharField(max_length=200)

    def __str__(self):
        return self.question[:20]

    def __unicode__(self):
        return self.question[:20]


class Quiz(Model):
    name = CharField(max_length=50)
    questions = ManyToManyField(Question)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Lesson(Model):
    lesson_number = IntegerField()
    video = CharField(null=True, default="", blank=True, max_length=200)
    text = TextField()
    title = CharField(max_length=50)
    quiz = OneToOneField(Quiz)
    description = TextField()

    def __str__(self):
        return str(self.lesson_number) + ". " + self.title

    def __unicode__(self):
        return str(self.lesson_number) + ". " + self.title


class LanguageArticle(Model):
    title = CharField(max_length=50)
    text = TextField()

class UserProfile(Model):
    user = OneToOneField(User)
    lessons = ManyToManyField(Lesson, null=True, default=None, blank=True)
    badges = ManyToManyField(Badge, null=True, default=None, blank=True)
    goals = ManyToManyField(Goal, null=True, default=None, blank=True)
    posts = ManyToManyField(Post, null=True, default=None, blank=True)

    def __str__(self):
        return self.user.email + " profile"

    def __unicode__(self):
        return self.user.email + " profile"
