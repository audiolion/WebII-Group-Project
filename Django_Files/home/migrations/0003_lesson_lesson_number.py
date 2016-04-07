# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160406_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
