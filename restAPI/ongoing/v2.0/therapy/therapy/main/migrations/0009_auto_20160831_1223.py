# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 12:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160831_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 31, 12, 23, 23, 616369, tzinfo=utc)),
        ),
    ]