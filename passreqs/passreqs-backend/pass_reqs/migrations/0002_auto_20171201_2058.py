# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pass_reqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='passreqs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passreqs', to='pass_reqs.PassReqs'),
        ),
    ]