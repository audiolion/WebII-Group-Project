# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_lesson_lesson_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
