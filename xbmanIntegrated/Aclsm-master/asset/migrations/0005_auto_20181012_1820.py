# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_people_roomasset'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomasset',
            options={'verbose_name': '\u65b0\u670d\u52a1\u5668\u8868', 'verbose_name_plural': '\u65b0\u670d\u52a1\u5668\u8868'},
        ),
        migrations.RenameField(
            model_name='roomasset',
            old_name='MaintenanceSn',
            new_name='name',
        ),
    ]
