# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0002_auto_20151014_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 18, 15, 32, 458884, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
