# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0005_auto_20160413_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 4, 18)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(default=b'', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 18)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 18)),
            preserve_default=True,
        ),
    ]
