# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20160502_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 5, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='replies',
            field=models.ManyToManyField(to='home.Reply', null=True, blank=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
