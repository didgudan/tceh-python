# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_address_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliablePizzaSizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=2)),
                ('full_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_size', to='pizza.AvaliablePizzaSizes'),
        ),
    ]
