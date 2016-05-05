# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160504_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='replies',
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(to='home.Post', default=0),
            preserve_default=False,
        ),
    ]
