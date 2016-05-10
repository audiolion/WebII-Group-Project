# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='description',
            field=models.CharField(max_length=200, default='Test'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 5, 9)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 9)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 9)),
            preserve_default=True,
        ),
    ]
