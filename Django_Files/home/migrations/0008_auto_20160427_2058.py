# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160420_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=datetime.date(2016, 4, 27)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 27)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reply',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 27)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='badges',
            field=models.ManyToManyField(default=None, to='home.Badge', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='goals',
            field=models.ManyToManyField(default=None, to='home.Goal', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lessons',
            field=models.ManyToManyField(default=None, to='home.Lesson', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='posts',
            field=models.ManyToManyField(default=None, to='home.Post', null=True, blank=True),
            preserve_default=True,
        ),
    ]
