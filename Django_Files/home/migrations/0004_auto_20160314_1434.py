# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0003_auto_20160310_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 3, 14)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 3, 14)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 3, 14)),
            preserve_default=True,
        ),
    ]
