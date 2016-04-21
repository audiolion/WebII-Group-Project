# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160418_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='progress',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lessons',
            field=models.ManyToManyField(default=None, to='home.Lesson', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 4, 20)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 20)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 20)),
            preserve_default=True,
        ),
    ]
