# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bcomment',
            field=models.ImageField(blank=True, null=True, default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=128, unique=True, db_index=True, db_column='title'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
    ]
