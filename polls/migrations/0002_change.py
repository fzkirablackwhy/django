# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_text', models.CharField(max_length=10)),
            ],
        ),
    ]
