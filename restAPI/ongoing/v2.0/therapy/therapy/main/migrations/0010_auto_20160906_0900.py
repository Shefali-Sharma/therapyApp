# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160831_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 6, 9, 0, 15, 873143, tzinfo=utc)),
        ),
    ]
