# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-10 21:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authoritys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(blank=True, choices=[(b'1', 'Empowerment'), (b'2', 'NoEmpowerment')], max_length=64, null=True, verbose_name='\u6743\u9650')),
                ('Auth_name', models.CharField(blank=True, max_length=64, verbose_name='app')),
            ],
            options={
                'verbose_name': '\u6743\u9650\u8868',
                'verbose_name_plural': '\u6743\u9650\u8868',
            },
        ),
        migrations.CreateModel(
            name='Weekly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeklys', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u91cd\u70b9\u5de5\u4f5c\u4e8b\u9879')),
                ('workplan', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5de5\u4f5c\u8ba1\u5212')),
                ('completion', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u672c\u5468\u8ba1\u5212\u5b8c\u6210\u60c5\u51b5')),
                ('coordination', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5de5\u4f5c\u96be\u70b9\u53ca\u6240\u9700\u534f\u8c03\u7684\u8d44\u6e90')),
                ('nextweek', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u4e0b\u5468\u5de5\u4f5c\u8ba1\u5212')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u8ba1\u5212',
                'verbose_name_plural': '\u5de5\u4f5c\u8ba1\u5212',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='\u90ae\u7bb1')),
                ('username', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='token')),
                ('department', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u90e8\u95e8')),
                ('tel', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u5ea7\u673a')),
                ('mobile', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u624b\u673a')),
                ('memo', models.TextField(blank=True, default=None, null=True, verbose_name='\u5907\u6ce8')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('valid_begin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f\u8868',
            },
        ),
        migrations.AddField(
            model_name='weekly',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AddField(
            model_name='authoritys',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
