# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190109_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 1, 9, 16, 56, 55, 67904, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime(2019, 1, 9, 16, 56, 55, 67279, tzinfo=utc)),
        ),
    ]
