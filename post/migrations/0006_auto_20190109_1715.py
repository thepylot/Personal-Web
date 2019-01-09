# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20190109_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 1, 9, 17, 15, 3, 435965, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime(2019, 1, 9, 17, 15, 3, 435325, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
