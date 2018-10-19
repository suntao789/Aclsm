#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'weihaoxuan'
from django.db import models
from django.contrib import admin
from Integrated.user_models import UserProfile

class Jump_user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(u'账户名称',max_length=30,blank=True, null=True)
    password = models.CharField(u'账户密码',max_length=30,blank=True, null=True)
    permiss = models.TextField(u'sudo权限')
    create_date = models.DateTimeField(editable=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name = '远程账户表'
        verbose_name_plural = "远程账户表"
    def __unicode__(self):
        return self.username

class Jump_group(models.Model):
    id = models.AutoField(primary_key=True)
    groupname = models.CharField(u'组名称',max_length=30,blank=True, null=True)
    user = models.ForeignKey('Jump_user', verbose_name=u'绑定账号',null=True, blank=True)
    dev_list = models.CharField(u'机器',max_length=9999,blank=True, null=True)
    create_date = models.DateTimeField(editable=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name = '机器分组表'
        verbose_name_plural = "机器分组表"
    def __unicode__(self):
        return self.groupname

class Jump_prem(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(UserProfile, verbose_name=u'用户名')
    group = models.ForeignKey(Jump_group, verbose_name=u'绑定组',null=True, blank=True)
    create_date = models.DateTimeField(editable=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name = '用户权限绑定表'
        verbose_name_plural = "用户权限绑定表"

class Jump_Notice(models.Model):
    name = models.CharField('通知内容', max_length=32)
    status = models.IntegerField('状态')
    create_date = models.DateTimeField(auto_now = True,blank=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '通知表'
        verbose_name_plural = "通知表"

class Jump_logs(models.Model):
    username = models.ForeignKey(UserProfile, verbose_name=u'用户名')
    ipaddress = models.GenericIPAddressField(u'IP', blank=True, null=True)
    file_path = models.CharField(u'日志文件路径', max_length=30, blank=True, null=True)
    create_date = models.DateTimeField(auto_now = True,blank=True)

    class Meta:
        verbose_name = '日志表'
        verbose_name_plural = "日志表"
admin.site.register(Jump_user)
admin.site.register(Jump_group)
admin.site.register(Jump_prem)
admin.site.register(Jump_Notice)
admin.site.register(Jump_logs)