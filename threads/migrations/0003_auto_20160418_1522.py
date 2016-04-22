# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20160418_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 14, 22, 36, 93000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(related_name='posts', to='threads.Thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 14, 22, 36, 91000, tzinfo=utc)),
        ),
    ]
