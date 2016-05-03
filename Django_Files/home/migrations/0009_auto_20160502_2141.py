# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20160427_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='badge',
            field=models.OneToOneField(blank=True, default=None, to='home.Badge', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badge',
            name='picture',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 5, 2)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(blank=True, max_length=200, default='', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 2)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 2)),
            preserve_default=True,
        ),
    ]
