# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0002_auto_20160309_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 3, 10)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 3, 10)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 3, 10)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='badges',
            field=models.ManyToManyField(default=None, to='home.Badge', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='goals',
            field=models.ManyToManyField(default=None, to='home.Goal', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='posts',
            field=models.ManyToManyField(default=None, to='home.Post', null=True),
            preserve_default=True,
        ),
    ]
