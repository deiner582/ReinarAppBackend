# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20150702_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(default=models.CharField(max_length=50), to=settings.AUTH_USER_MODEL),
        ),
    ]
