# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagem'),
        ),
    ]
