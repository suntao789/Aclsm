# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20181012_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=64, verbose_name='\u59d3\u540d')),
                ('PhoneNumber', models.CharField(max_length=30, null=True, verbose_name='\u7535\u8bdd\u53f7\u7801', blank=True)),
            ],
            options={
                'verbose_name': '\u5f55\u5165\u4eba\u5458',
                'verbose_name_plural': '\u5f55\u5165\u4eba\u5458\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='RoomAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_type', models.CharField(default=b'server', max_length=64, choices=[(b'server', '\u7269\u7406\u670d\u52a1\u5668')])),
                ('MaintenanceSn', models.CharField(max_length=64, verbose_name='\u8fd0\u7ef4\u8d44\u4ea7\u7f16\u53f7')),
                ('Sn', models.CharField(unique=True, max_length=128, verbose_name='\u8d44\u4ea7SN\u53f7')),
                ('Brand', models.CharField(max_length=128, null=True, verbose_name='\u5236\u9020\u5546\u54c1\u724c', blank=True)),
                ('Model', models.CharField(max_length=128, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('ServerConfig', models.CharField(max_length=256, null=True, verbose_name='\u670d\u52a1\u5668\u914d\u7f6e', blank=True)),
                ('Cabinet', models.CharField(max_length=128, null=True, verbose_name='\u673a\u67dc', blank=True)),
                ('Slot', models.CharField(max_length=128, null=True, verbose_name='\u69fd\u4f4d', blank=True)),
                ('ServiceModule', models.CharField(max_length=128, null=True, verbose_name='\u670d\u52a1\u6a21\u5757', blank=True)),
                ('System', models.CharField(max_length=128, null=True, verbose_name='\u7269\u7406\u673a\u7cfb\u7edf', blank=True)),
                ('RaidInfo', models.CharField(max_length=128, null=True, verbose_name='Raid\u5361\u4fe1\u606f', blank=True)),
                ('MacInfo', models.CharField(max_length=128, null=True, verbose_name='MAC\u4fe1\u606f', blank=True)),
                ('TorCabinet', models.CharField(max_length=128, null=True, verbose_name='TOR\u673a\u67dc', blank=True)),
                ('ilo', models.GenericIPAddressField(null=True, verbose_name=b'ilo IP', blank=True)),
                ('SubnetMask', models.CharField(max_length=128, null=True, verbose_name='\u5b50\u7f51\u63a9\u7801', blank=True)),
                ('Gateway_ip', models.GenericIPAddressField(null=True, verbose_name='\u7f51\u5173 IP', blank=True)),
                ('Inband_ip', models.GenericIPAddressField(null=True, verbose_name='\u5e26\u5185 IP', blank=True)),
                ('Inband_SubnetMask', models.CharField(max_length=128, null=True, verbose_name='\u5e26\u5185IP\u5b50\u7f51\u63a9\u7801', blank=True)),
                ('Inband_Gateway_ip', models.GenericIPAddressField(null=True, verbose_name='\u5e26\u5185\u7f51\u5173 IP', blank=True)),
                ('BGP_ip', models.GenericIPAddressField(null=True, verbose_name='BGP IP', blank=True)),
                ('BGP_SubnetMask', models.CharField(max_length=128, null=True, verbose_name='BGP IP\u5b50\u7f51\u63a9\u7801', blank=True)),
                ('BGP_Gateway_ip', models.GenericIPAddressField(null=True, verbose_name='BGP\u7f51\u5173 IP', blank=True)),
                ('trade_date', models.DateField(null=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4', blank=True)),
                ('expire_date', models.DateField(null=True, verbose_name='\u8fc7\u4fdd\u4fee\u671f', blank=True)),
                ('status', models.CharField(default=b'start', max_length=64, verbose_name='\u72b6\u6001', choices=[(b'start', '\u5728\u7528'), (b'Disable', '\u505c\u7528\u672a\u4e0b\u67b6'), (b'Disable_down', '\u505c\u7528\u5df2\u4e0b\u67b6'), (b'maintain', '\u7ef4\u4fee')])),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('Owner', models.ForeignKey(verbose_name='\u5f55\u5165\u4eba\u5458', blank=True, to='asset.People', null=True)),
                ('idc', models.ForeignKey(verbose_name='IDC\u673a\u623f', blank=True, to='asset.IDC', null=True)),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
    ]
