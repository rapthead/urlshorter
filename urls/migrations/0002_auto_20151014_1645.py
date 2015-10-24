# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='hash',
            field=models.CharField(unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=65535, validators=[django.core.validators.URLValidator([b'http', b'https'])]),
        ),
    ]
