# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20181011_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufactory',
            old_name='server_config',
            new_name='memo',
        ),
        migrations.RenameField(
            model_name='manufactory',
            old_name='model',
            new_name='support_num',
        ),
    ]
