# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_auto_20150702_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
