# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cineFast', '0012_auto_20160508_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diretor',
            old_name='file',
            new_name='foto',
        ),
    ]