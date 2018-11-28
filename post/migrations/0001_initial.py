# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=200, choices=[(b'mobile', b'MOBILE'), (b'software', b'SOFTWARE'), (b'game', b'GAME'), (b'space', b'SPACE'), (b'science', b'SCIENCE'), (b'social media', b'SOCIAL MEDIA'), (b'equipment', b'EQUIPMENT')])),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
