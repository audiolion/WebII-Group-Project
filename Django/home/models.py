import datetime
from django.db.models import Model

from django.contrib.auth.models import User

from django.db.models.fields import IntegerField, CharField, DateField, BooleanField, TextField
from django.db.models.fields.files import ImageField, FileField
from django.db.models.fields.related import ManyToManyField, OneToOneField, ForeignKey


class Badge(Model):
    name = CharField(max_length=50)
    picture = ImageField()


class Goal(Model):
    start_date = DateField(default=datetime.date.today())
    end_date = DateField(default=None, null=True)
    lessons_completed = IntegerField(default=None, null=True)
    remind_me = BooleanField(default=True)


class Reply(Model):
    user = OneToOneField(User)
    text = TextField()
    date = DateField(default=datetime.date.today())

    def __unicode__(self):
        return u'{0}\n{1}'.format(self.user.username, self.text[:50])


class Post(Model):
    user = OneToOneField(User)
    text = TextField()
    #Upvote/Stars/Karma
    replies = ManyToManyField(Reply)
    date = DateField(default=datetime.date.today())

    def __unicode__(self):
        return u'{0}\n{1}'.format(self.user.username, self.text[:50])


class Question(Model):
    question = TextField()
    answer1 = CharField(max_length=200)
    answer2 = CharField(max_length=200)
    answer3 = CharField(max_length=200)
    answer4 = CharField(max_length=200)
    correct_answer = CharField(max_length=5)


class Quiz(Model):
    name = CharField(max_length=50)
    questions = ManyToManyField(Question)


class Lesson(Model):
    video = FileField()
    text = TextField()
    title = CharField(max_length=50)
    quiz = OneToOneField(Quiz)


class UserProfile(Model):
    user = OneToOneField(User)
    progress = IntegerField(default=0)
    badges = ManyToManyField(Badge)
    goals = ManyToManyField(Goal)
    posts = ManyToManyField(Post)
