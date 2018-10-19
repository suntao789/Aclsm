# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20181012_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomasset',
            name='nic1',
            field=models.CharField(max_length=32, null=True, verbose_name='\u4e07\u5146\u7f51\u53e31', blank=True),
        ),
        migrations.AddField(
            model_name='roomasset',
            name='nic2',
            field=models.CharField(max_length=32, null=True, verbose_name='\u4e07\u5146\u7f51\u53e32', blank=True),
        ),
        migrations.AddField(
            model_name='roomasset',
            name='nic3',
            field=models.CharField(max_length=32, null=True, verbose_name='\u4e07\u5146\u7f51\u53e33', blank=True),
        ),
        migrations.AddField(
            model_name='roomasset',
            name='nic4',
            field=models.CharField(max_length=32, null=True, verbose_name='\u4e07\u5146\u7f51\u53e34', blank=True),
        ),
        migrations.AddField(
            model_name='roomasset',
            name='nic5',
            field=models.CharField(max_length=32, null=True, verbose_name='\u4e07\u5146\u7f51\u53e35', blank=True),
        ),
        migrations.AddField(
            model_name='roomasset',
            name='nic6',
            field=models.CharField(max_length=32, null=True, verbose_name='\u4e07\u5146\u7f51\u53e36', blank=True),
        ),
        migrations.AlterField(
            model_name='roomasset',
            name='BGP_SubnetMask',
            field=models.CharField(max_length=64, null=True, verbose_name='BGP IP\u5b50\u7f51\u63a9\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='roomasset',
            name='Inband_SubnetMask',
            field=models.CharField(max_length=64, null=True, verbose_name='\u5e26\u5185IP\u5b50\u7f51\u63a9\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='roomasset',
            name='SubnetMask',
            field=models.CharField(max_length=64, null=True, verbose_name='\u5b50\u7f51\u63a9\u7801', blank=True),
        ),
    ]
