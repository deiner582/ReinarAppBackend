# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(default='d', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
