# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-27 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('credit_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=16)),
                ('cust_code', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=32)),
                ('create_date', models.DateField(auto_now=True)),
                ('cust_state', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('mobile', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='credit',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.Cust'),
        ),
    ]
