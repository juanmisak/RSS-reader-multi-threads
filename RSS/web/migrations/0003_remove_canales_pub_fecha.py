# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150615_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canales',
            name='pub_fecha',
        ),
    ]
