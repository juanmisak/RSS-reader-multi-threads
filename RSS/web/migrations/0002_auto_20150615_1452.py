# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canales',
            name='descripcion',
            field=models.CharField(default=datetime.datetime(2015, 6, 15, 14, 52, 0, 559889, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canales',
            name='pub_fecha',
            field=models.CharField(default=datetime.datetime(2015, 6, 15, 14, 52, 13, 921643, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
