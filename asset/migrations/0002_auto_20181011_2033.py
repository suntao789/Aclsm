# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufactory',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='manufactory',
            name='support_num',
        ),
        migrations.AddField(
            model_name='manufactory',
            name='model',
            field=models.CharField(max_length=30, verbose_name='\u578b\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='manufactory',
            name='server_config',
            field=models.CharField(max_length=128, verbose_name='\u670d\u52a1\u5668\u914d\u7f6e', blank=True),
        ),
    ]
